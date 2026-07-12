import os
import logging
from dotenv import load_dotenv

# 1. ALWAYS load environment variables before importing modules that need them
load_dotenv()
# Custom application imports
from config import AppConfig
import validators
from ollama import Client

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
            
        print()  # Print a clean newline at the very end of the stream, not on every token iteration
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
        
        # Run pre-execution constraints check
        task = validators.validate_user_prompt(prompt)
        
        # Initiate secure streaming token transfer
        execute_model_call(task)
        
    except ValueError as val_err:
        logging.warning(f"Validation failed: {val_err}")
    except AIApplicationError as app_err:
        logging.error(f"Application error caught: {app_err}")


if __name__ == "__main__":
    get_prompt()
