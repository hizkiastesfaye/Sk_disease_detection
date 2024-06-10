from openai import OpenAI
import os
from pathlib import Path
import httpx
from hyperon import *
import re

proxy=os.environ.get('OPENAI_PROXY')
clien = OpenAI() if proxy is None else \
         OpenAI(http_client=httpx.Client(proxies=proxy))

message = "Below is a user's question and the answer for the user's question. By getting a context from the user's question, make the response more descriptive. You can get an accurate information from the dataset that's provided below when generating more descriptions.\n\
    \nFind the Gene Ontology (GO) categories associated with protein Q13461\n\
    \nReturn only the response you generated based on this datasset {fil} by adding more description in paragrph. \n"
messages = [{'role':'user','content':str(message)}]

def gpt (messages,function = [],model="gpt-3.5-turbo-0613"):
    client = clien.chat.completions.create(
        model = model,
        messages=messages,
        temperature=0,
        timeout=15
    )
    return client

response = gpt(messages)
print(response.choices[0].message.content)