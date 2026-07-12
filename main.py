import os
from dotenv import load_dotenv
import logging
import config
import validators
# This loads the variables from your .env file into the system environment
load_dotenv()
from ollama import Client

def execute_model_call(task:str)-> str:

 client = Client(
    host=config.HOST,
    headers={'Authorization': 'Bearer ' + config.API_KEY}
 )

 if(len(task)==0 or task.isdigit()):
     raise ValueError("task cannot be a negative number!")

 messages = [
   {
    'role': 'user',
    'content': f'Breakdown this task : {task} into goals',
   },
 ]
 for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)

def get_prompt(prompt:str)-> str:
  task =input("Enter the task you want to break down: ")
  task=validators.validate_user_prompt(prompt)
  message=execute_model_call(task)
 

