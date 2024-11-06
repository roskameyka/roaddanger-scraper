import requests
import json
from keys import *
import ollama


async def makeCompute(messages: list, model: str = "llama3.2", local: bool =True):
  if not local:
    response =  await requests.post(
      url="https://openrouter.ai/api/v1/chat/completions",
      headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
      },
      data=json.dumps({
        "model": model, # Optional
        "messages": messages
      })
    )
    # Check if the request was successful
    if response.status_code == 200:
        # Print the response from the model
        result = response.json()
        print(result["text"])
        return result["text"]
        
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
  else:
    result = await ollamaMakeComute(messages=messages, model=model)
    return result['message']['content']
def ollamaMakeComute(messages: list, model: str = "llama3.2"):
  return  ollama.chat(model=model, messages=messages)
  