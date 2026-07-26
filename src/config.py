import os
from dotenv import load_dotenv

# Force Python to read your local .env file
load_dotenv()

class AppConfig:
    """This class contains configuration and api-keys"""
    API_KEY = os.environ.get('OLLAMA_API_KEY')
    
    # Safely convert to numeric types by parsing the environment strings
    MAX_PROMPT_CHARS = int(os.environ.get('MAX_PROMPT_CHARS', 500))
    TIMEOUT_SECONDS = float(os.environ.get('TIMEOUT_SECONDS', 30.0))
    HOST = os.environ.get('HOST')
    MODEL_TAG = os.environ.get('MODEL_TAG')

    @classmethod
    def validate(cls):
        if cls.API_KEY is None or len(cls.API_KEY) == 0:
            raise RuntimeError("Missing key")
            
        if not cls.MAX_PROMPT_CHARS or not isinstance(cls.MAX_PROMPT_CHARS, int):
            raise RuntimeError("Missing or invalid MAX_PROMPT_CHARS")
            
        if not cls.TIMEOUT_SECONDS or not isinstance(cls.TIMEOUT_SECONDS, float):
            raise RuntimeError("Missing or invalid TIMEOUT_SECONDS")
            
        if not cls.HOST or not isinstance(cls.HOST, str):
            raise RuntimeError("Missing or invalid Host")
        
        if not  cls.MODEL_TAG or not isinstance(cls.MODEL_TAG,str):
            raise RuntimeError("Missing model tag")

# Run the validation check automatically when this file is imported
AppConfig.validate()
