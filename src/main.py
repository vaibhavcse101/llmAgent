import os
import logging
from dotenv import load_dotenv
from src.config import AppConfig
from src.validators import validate_user_prompt
from ollama import Client
from src.resiliance import (
    AIApplicationError,
    APIConnectionTimeoutError,
    ProviderRateLimitError
)
# Configure logging style
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def execute_model_call(task: str) -> str:
    """Connects to the Ollama client infrastructure and handles streamed output loops."""
    try:
        # FIX: Changed Java style 'config.HOST' to Python class 'AppConfig.HOST'
        client = Client(
            host=AppConfig.HOST,
            headers={'Authorization': f'Bearer {AppConfig.API_KEY}'}
        )

        # FIX: Handled validation logic cleanly without Java-style parentheses
        if not task or task.isdigit():
            raise ValueError("Task cannot be blank or entirely composed of digits!")

        messages = [
            {
                'role': 'user',
                'content': f'Breakdown this task: {task} into goals',
            },
        ]
        
        full_response = ""
        
        # Stream evaluation block
        # FIX: Indented the entire block precisely to exactly 8 spaces inside the try-block
        for part in client.chat(AppConfig.MODEL_TAG, messages=messages, stream=True):
            content = part['message']['content']
            print(content, end='', flush=True)
            full_response += content
            
        print()
        return full_response

    except Exception as exc:
        if "timeout" in str(exc).lower():
            raise APIConnectionTimeoutError("AI Model response timed out.") from exc
        if "rate limit" in str(exc).lower() or "429" in str(exc):
            raise ProviderRateLimitError("Rate limit exceeded on provider endpoint.") from exc
        raise AIApplicationError(f"Unexpected provider dependency issue: {exc}") from exc


def get_prompt():
    """Application orchestration entry point managing user console interaction loops."""
    try:
        prompt = input("Enter the task you want to break down: ")
        print(prompt)

        # Run pre-execution constraints check
        task = validate_user_prompt(prompt)
        print(task)
        # Initiate secure streaming token transfer
        return execute_model_call(task)
        
    except ValueError as val_err:
        logging.warning(f"Validation failed: {val_err}")
    except AIApplicationError as app_err:
        logging.error(f"Application error caught: {app_err}")


if __name__ == "__main__":
    AppConfig.validate()
    get_prompt()
    
