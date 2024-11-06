# validation of method
# try to reproduce roaddangers findings with llm


import os, json
import pandas as pd
from testcases import *
from llm import *
import asyncio

models=[
  "openai/o1-mini",
  "llama3.2"
]
model = models[1]
local = True

path_to_json = 'test_data/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
 

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        print(f'Article: {json_text["id"]} scores {json_text["roaddanger_dehumanisation_score"]} in roaddangers dehumanisation score')
        prompt_message = [
            {
             'role': 'user',
             'content':  f"""
                            {roaddanger_dehumanisation_eval} 
                            Only return the answer as a number.
                            Here is the article:
                            Sample artilce with no information
              """
            },
            {
             'role': "assistant",
             "content": "'{'dehumanisation': '0'}'"
            },
            {
            'role': 'user',
            'content': f"""
                            {roaddanger_dehumanisation_eval} 
                            return a number. 
                            Here is the article:
                            {json_text['articles'][0]["title"]} 
                            {json_text['articles'][0]["summary"] if not json_text['articles'][0]["alltext"] else json_text['articles'][0]["alltext"]}
              """
            },
        ]
        response = makeCompute(prompt_message, model=model, local=local)
        try:
          msg = json.loads(response)
          print(msg["dehumanisation"])
        except Exception as e:
          # reflect if the format 
          prompt_message.append({
            'role': 'user',
            "content": f'{response} is not in valid json format. Print it correctly error: {e}'
          }) 
          response = makeCompute(prompt_message, model=model)
        
        
        print(f"Model {model} eval is { response}")
