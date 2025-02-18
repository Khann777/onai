import requests
from decouple import config

OPENROUTER_API_KEY = config("OPENROUTER_API_KEY")

def send_to_llm(message: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
    }

    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    return response_json["choices"][0]["message"]["content"]
