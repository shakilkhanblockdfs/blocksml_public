import requests
import os
import time
import math

# For Linux add the following line to ollama-custom-models.conf
# Environment="OLLAMA_HOST=0.0.0.0"
# For Mac run the following commands on mac
# launchctl setenv OLLAMA_HOST "0.0.0.0"

url = "http://localhost:11434/api/generate"


def question_answer(question):
    data = {
        "model": "llama2",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=data)

    # Check the response status code
    if response.status_code == 200:
        # Print the response content
        return (response.json()['response'])
        #print(type(response))
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}, {response.text}")


# question = "Why does light scatter"
# question = "Name some famous asteroid"
question = "Name some Hollywood movies where Irfan Khan was an actor or co-actor"

response = question_answer(question)
print(response)
