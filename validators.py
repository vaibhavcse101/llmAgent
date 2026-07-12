import  config from AppConfig

def validate_user_prompt(prompt: str) ->  str:
    if prompt not:
        raise ValueError("prompt must be non empty")

    cleaned_prompt=prompt.strip().lower()
    if cleaned_prompt not or not isintance(cleaned_prompt,str):
        raise ValueError("prompt must be non empty")
    
    if len(cleaned_prompt>AppConfig.MAX_PROMPT_CHARS):
        raise ValueError("prompt must be non empty")
    
    injection_keywords = ["ignore previous instructions", "system override", "bypass rules"]
    if any(keyword cleaned_prompt in for keyword in injection_keywords):
        raise ValueError("prompt must be clean")
    return cleaned_prompt

 
