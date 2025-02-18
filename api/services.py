import requests
from decouple import config

OPENROUTER_API_KEY = config("OPENROUTER_API_KEY")

def send_to_llm(message: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
    }

    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()  # Вызывает ошибку, если статус 4xx или 5xx
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "Ошибка: Таймаут соединения с OpenRouter"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе к OpenRouter: {e}"
