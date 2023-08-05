from typing import List, Callable, Dict, Union
from uuid import uuid5, NAMESPACE_DNS, UUID
from abc import ABC, abstractmethod
import tiktoken
import logging


DEFAULT_CACHE_KEY="default"

class NotFoundHandle:
    def __init__(self, cache_namespace_key, prompt, embedding):
        self.prompt = prompt
        self.embedding = embedding
        self.cache_namespace_key = cache_namespace_key
    
    def __bool__(self):
        return False
    

class PromptWatchCache:
    def __init__(self, cache_namespace_key, implementation:"CacheImplBase", embed_func:Callable[[str],List[float]], token_limit, similarity_limit:float=0.95):
        self.cache_namespace_key = cache_namespace_key
        self.implementation:CacheImplBase= implementation
        self.embed_func = embed_func
        self.similarity_limit=similarity_limit
        self.token_limit=token_limit
        self.logger = logging.getLogger(__name__)
        self._last_prompt = None
        self._last_prompt_ignore = False

    def test_token_limit(self, prompt:str)->bool:
         # assuming that the average token length is way over 2 chars, it's safe to assume that if the prompt is half the token limit, we the real limit won't be reached
        if len(prompt)/2 <= self.token_limit:
            return True
        elif num_tokens_from_string(prompt) <= self.token_limit:
            return True
        else:
            return False
        

    def get(self, prompt:str)->Union[str, NotFoundHandle,None]:
        """ returns cached str if found, NotFoundHandle if not found, None if prompt is too long to be cached
        
        ## Example usage:
        
        ```
        cached_result = cache.get("foo")
        if not cached_result:
            result = llm.run("foo")
            cache.add(cached_result,result)
        else:
            return cached_result
        ```
        """
        try:
            if self.test_token_limit(prompt):
                prompt_embedding = self.embed_func(prompt)
                result = self.implementation.get(prompt_embedding,self.similarity_limit)
                if result is None:
                    return NotFoundHandle(self.cache_namespace_key, prompt, prompt_embedding)
            else:
                self.logger.warning(f"Prompt {prompt} is too long to be cached. It will be ignored")
                return None
        except Exception as e:
            self.logger.warn(f"Skipping cache due to Error: {e}")
    

    def add(self, not_found_handle: NotFoundHandle, result:str):
        # not_found_handle could be None (too long prompt), in which case we ignore it
        if isinstance(not_found_handle,NotFoundHandle):
            try:
                if not_found_handle.cache_namespace_key != self.cache_namespace_key:
                    raise ValueError("PromptWatchCache.add called with a not_found_handle that does not belong to this cache")
                prompt_hash = uuid5(NAMESPACE_DNS, not_found_handle.prompt)
                self.implementation.add(prompt_hash, not_found_handle.embedding, result)
            except Exception as e:
                self.logger.warn(f"Failed storing prompt into cache {e}")
        
    



class PromptWatchCacheManager:

    def __init__(self, promptwatch_context):
        self.promptwatch_context = promptwatch_context
        self.caches:Dict[str, PromptWatchCache] = {}
        

    def init_cache(self, cache_namespace_key:str=None, local:bool=False, embed_func:Callable[[str],List[float]]=None, token_limit=None, langchain_embeddings=None, similarity_limit=0.95):
        if not cache_namespace_key:
            cache_namespace_key = DEFAULT_CACHE_KEY
        if not embed_func:
            if not langchain_embeddings:
                try: 
                    import openai
                    
                    token_limit = 8191 #token limit for ada-002

                    def embed(prompt:str)->List[float]:
                        # replace newlines, which can negatively affect performance.
                        prompt = prompt.replace("\n", " ")
                        engine='text-embedding-ada-002'
                        return openai.Embedding.create(input=[prompt], engine=engine)["data"][0]["embedding"]
                    embed_func = embed
                except ImportError:
                    raise Exception("Unable to import default embeddings provider (OpenAI). Please install openai (pip install openai) or provide either an embed_func or a langchain_embeddings instance")
            else:

                if not token_limit:
                    raise Exception("token_limit must be provided if langchain_embeddings is provided")
                
                if not hasattr(langchain_embeddings,"embed_query"):
                    raise Exception("langchain_embeddings must have an embed_query method")
                
                def embed(prompt:str)->List[float]:
                    return langchain_embeddings.embed_query(prompt)
                embed_func = embed
        if local:
            self.caches[cache_namespace_key] = PromptWatchCache(cache_namespace_key, LocalImpl(cache_namespace_key, embed_func), embed_func, token_limit=token_limit, similarity_limit=similarity_limit)

    def get_cache(self, cache_namespace_key=None)->PromptWatchCache:
        cache_namespace_key=cache_namespace_key or DEFAULT_CACHE_KEY
        if not cache_namespace_key in self.caches:
            raise Exception(f"Cache {cache_namespace_key} not initialized")
        return self.caches[cache_namespace_key]


class CacheImplBase(ABC):

    def __init__(self, cache_namespace_key:str =None) -> None:
        self.cache_namespace_key = cache_namespace_key

    @abstractmethod
    def get(self, prompt_embedding:List[float], limit:float = 0.95)-> str:
        pass
    
    @abstractmethod
    def add(self, prompt_hash:UUID, prompt_embedding:List[float],result:str):
        pass
    


class LocalImpl(CacheImplBase):
    def __init__(self, cache_namespace_key:str =None,embed_func=None ) -> None:
        try:
            from langchain.vectorstores.chroma import Chroma
            import chromadb
            from chromadb.config import Settings
            from chromadb.api.local import LocalAPI
            from chromadb.api.local import Collection
            
            client:LocalAPI = chromadb.Client(Settings(chroma_db_impl="duckdb", persist_directory=f"promptwatch_cache/{cache_namespace_key}"))
            collection = client.get_or_create_collection(name=cache_namespace_key or DEFAULT_CACHE_KEY, embedding_function=embed_func or (lambda x:[]))
            
            self.collection:Collection = collection
            self.has_data = self.collection.count()>0
            
            
        except ImportError:
            raise ImportError("chromadb is required for local cache... please use 'pip install chromadb'")
    

    def get(self, prompt_embedding:List[float], limit:float = 0.95)-> str:
        if self.has_data:
            results =  self.collection.query(query_embeddings=[prompt_embedding],n_results=1)
            docs = results["documents"]
            if docs:
                return docs[0]
            

    def add(self, prompt_hash:UUID, prompt_embedding:List[float],result:str):
        
        self.collection.add(
            embeddings=[prompt_embedding],
            documents=[result],
            ids=[str(prompt_hash)],
        )
        
        self.has_data=True


def num_tokens_from_string(string: str, encoding_name: str="cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
