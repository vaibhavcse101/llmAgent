from config import AppConfig

def validate_user_prompt(prompt: str) -> str:
    # 1. Check for None input safely
    if prompt is None:
        raise ValueError("Prompt must be non-empty")

    cleaned_prompt = prompt.strip().lower()
    
    # 2. Check for empty strings after trimming whitespace
    if len(cleaned_prompt) == 0:
        raise ValueError("Prompt must be non-empty")
    
    # 3. Fixed misplaced parenthesis for character limit check
    if len(cleaned_prompt) > AppConfig.MAX_PROMPT_CHARS:
        raise ValueError(f"Prompt exceeds max limit of {AppConfig.MAX_PROMPT_CHARS} characters!")
    
    # 4. Corrected syntax for the prompt injection scan loop
    injection_keywords = ["ignore previous instructions", "system override", "bypass rules"]
    if any(keyword in cleaned_prompt for keyword in injection_keywords):
        raise ValueError("Prompt must be clean")
        
    return cleaned_prompt
