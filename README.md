# llmAgent
A basic level python-based application which takes an user input (task) and breaks it down into achievable goals

---

## 🚀 Setup & Local Execution

### 1. Prerequisites
Ensure you have Python 3.12+ installed on your system.
An Ollama cloud account and API key

### 2. Environment Setup
Clone the repository and spin up an isolated virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```
Create a .env file in the project root with following config:
```
OLLAMA_API_KEY=<your-cloud-api-key>
MAX_PROMPT_CHARS=500
TIMEOUT_SECONDS=30
HOST=https://ollama.com
MODEL_TAG=gpt-oss:120b
```

### 3. Run the Application
Execute the command-line orchestrator:
```bash
python -m src.main
```

### 4. Usage
When the program starts enter the task , you want to break down 
The output would be the task broken down into goals

---

## 📈 Running the Test Suite

Execute the entire unit and validation test suite from the root project directory:
```bash
python -m pytest -v
```


