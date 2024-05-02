import os
from groq import Groq
groq_api_key = "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"

def prompt_llama(msg:str) -> str:
    client = Groq(              # Setup a Client
        api_key = groq_api_key
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": msg,
            }
        ],
        model="llama3-70b-8192",
    )
    text_generated = chat_completion.choices[0].message.content
    
    try:
        text_generated = text_generated.split('\n')[2:]  # Skip the introductory statement "Here is what you asked: "
        text_generated = '\n'.join(text_generated)
    except:
        pass
    
    return text_generated