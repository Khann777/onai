from celery import shared_task
import requests
from .models import ChatHistory
from .services import send_to_llm

@shared_task
def process_webhook(message: str, callback_url: str):
    response_text = send_to_llm(message)
    ChatHistory.objects.create(user_message=message, bot_response=response_text)
    requests.post(callback_url, json={"response": response_text})
