# Example of an OpenAI ChatCompletion request with stream=True
# https://platform.openai.com/docs/api-reference/streaming#chat/create-stream

# imports
import time  # for measuring time duration of API calls
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_open_ai_response(question):
    # a ChatCompletion request
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': question}
        ],
        temperature=0,
        stream=True  # this time, we set stream=True
    )
    return response

question = "Why does light scatter"
# question = "Name some famous asteroid"
# question = "Name some Hollywood movies where Irfan Khan was an actor or co-actor"

response = get_open_ai_response(question)
for chunk in response:
    print((chunk.choices[0].delta.content), end='', flush=True)
