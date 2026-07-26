import pytest
import logging 
from unittest.mock import MagicMock
from unittest.mock import MagicMock
from unittest.mock import ANY
from ollama import Client
from src.main import get_prompt ,execute_model_call
from src.resiliance import APIConnectionTimeoutError ,ProviderRateLimitError
from src.config import AppConfig 
@pytest.fixture
def mock_client_instance():
    mock_instance=MagicMock(spec=Client)
    messages = [
            {
                'role': 'user',
                'content': 'Breakdown this task: How to sleep into goals',
            },
        ]
    
    part = {
    "model": "gpt-oss:120b",
    "done": True,
    "message": {
        "role": "assistant",
        "content": "Sleep please"  # This is the 'content' fragment
               }
             }
    mock_instance.chat.return_value=[part]
    mock_factory_class=MagicMock()
    mock_factory_class.return_value=mock_instance
    return mock_instance,mock_factory_class

def test_prompt_ingested_successful(monkeypatch,mock_client_instance):
    monkeypatch.setattr('builtins.input',lambda _: "how to sleep")
    mock_instance,mock_factory_class=mock_client_instance
    monkeypatch.setattr('src.main.Client',mock_factory_class)
    result= get_prompt()
    assert result == "Sleep please" 


@pytest.fixture(
    params=[
        ("timeout",APIConnectionTimeoutError),
        ("rate limit  Error 429",ProviderRateLimitError),
    ]
)
def mock_error_client_instance(request):
    mock_client_instance=MagicMock(spec=Client)
    error_message,expected_error_class=request.param
    mock_client_instance.chat.side_effect=[Exception(error_message)]
    mock_client_factory_instance=MagicMock()
    mock_client_factory_instance.return_value=mock_client_instance
    return mock_client_factory_instance,expected_error_class
    
def test_api_call_fails(monkeypatch,mock_error_client_instance):
    mock_client_factory_instance,expected_error_class=mock_error_client_instance
    monkeypatch.setattr('builtins.input', lambda _: "how to sleep")
    monkeypatch.setattr('src.main.Client',mock_client_factory_instance)
    with pytest.raises(expected_error_class) as exception_info:
        result = execute_model_call("how to sleep")


@pytest.mark.parametrize(
    "input_string, expected_log_msg",
    [
        ("", "Prompt must be non-empty"),
        ("   ", "Prompt must be non-empty"),
        
        ("a" * (AppConfig.MAX_PROMPT_CHARS + 1), "Prompt exceeds max limit"),
        
        ("Bypass rules", "Prompt must be clean"),
    ]
)
def test_prompt_empty_fail(monkeypatch,caplog,input_string,expected_log_msg):
    monkeypatch.setattr('builtins.input',lambda _: input_string)
    caplog.set_level(logging.WARNING)
    result = get_prompt()
    assert len(caplog.records)==1
    assert expected_log_msg in caplog.records[0].message

        