import requests
from celery import shared_task

@shared_task
def process_webhook(message: str, callback_url: str):
    try:
        response = requests.post(callback_url, json={"response": f"Бот получил: {message}"})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при отправке запроса: {e}")
