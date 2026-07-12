import os 

class AppConfig:
   """ This class contains api-keys"""
   API_KEY=os.environ.get('OLLAMA_API_KEY')
   MAX_PROMPT_CHARS = int(os.environ.get('MAX_PROMPT_CHARS'))
   TIMEOUT_SECONDS  = floats(os.environ.get('TIMEOUT_SECONDS'))
   HOST=os.environ.get('HOST')

   @classMethod
   def validate(cls):
    if(null == cls.API_KEY or len(cls.API_KEY)==0 ):
        raise RuntimeError("Missing key")
    if not MAX_PROMPT_CHARS or not isinstance(MAX_PROMPT_CHARS,int):
        raise RuntimeError("Missing or invalid MAX_PROMPT_CHARS")
    if not TIMEOUT_SECONDS or not isinstance(TIMEOUT_SECONDS,float):
        raise RuntimeError("Missing or invalid TIMEOUT_SECONDS")
    if not HOST or not isinstance(HOST,str):
        raise RuntimeError("Missing or invalid Host")
