import os
import requests
from dotenv import load_dotenv

load_dotenv()


def generate_letter(prompt, word_count):

    headers = {
        'Authorization': f'Bearer {os.environ["OPENAI_API_KEY"]}',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': word_count + 30,
    }

    response = requests.post(
        os.environ["OPENAI_API_URL"],
        headers=headers,
        json=payload
    )

    api_response = response.json()
    res = api_response["choices"][0]["text"]

    return res
