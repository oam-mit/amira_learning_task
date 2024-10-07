from openai import OpenAI

from dotenv import load_dotenv

import os

import json

load_dotenv()

def get_response(chat_history=[]):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    with open("prompt.txt") as fp:
        content = fp.read()

    chat_history = [{
        "role":chat["role"],
        "content":[
            {
                "type":"text",
                "text":chat["content"]
            }
        ]
    } for chat in chat_history]

    messages = [{
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": content
                    }
                ]
            }]
    
    messages.extend(chat_history)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1.24,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "json_object"
        },
    )


    return json.loads(response.choices[0].message.content)