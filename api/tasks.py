import requests
from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def process_webhook(message: str, callback_url: str):
    try:
        logger.debug(f"Отправка запроса на {callback_url} с данными: {message}")
        print(f"Отправка запроса на {callback_url} с данными: {message}")  # Временный лог

        response = requests.post(callback_url, json={"response": f"Бот получил: {message}"}, timeout=5)

        response.raise_for_status()
        logger.debug(f"Успешно отправлено. Код ответа: {response.status_code}")
        print(f"Успешно отправлено. Код ответа: {response.status_code}")

        return response.json()
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Ошибка соединения: {e}")
        print(f"Ошибка соединения: {e}")
        return {"error": f"Ошибка соединения: {e}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при отправке запроса: {e}")
        print(f"Ошибка при отправке запроса: {e}")
        return {"error": str(e)}
