import pytest
from rest_framework.test import APIClient
from unittest.mock import patch

@pytest.mark.django_db
@patch("api.tasks.process_webhook.delay")
def test_webhook_endpoint(mock_celery_task):
    client = APIClient()
    data = {"message": "Привет, бот!", "callback_url": "https://example.com/callback"}
    response = client.post("/webhook/", data, format="json")

    # Выводим лог ошибки, если тест падает
    if response.status_code != 202:
        print("Ошибка! Ответ API:", response.data)

    assert response.status_code == 202
    mock_celery_task.assert_called_once_with("Привет, бот!", "https://example.com/callback")


@pytest.mark.django_db
def test_webhook_no_callback_url():
    client = APIClient()
    data = {"message": "Привет, бот!"}
    response = client.post("/webhook/", data, format="json")

    assert response.status_code == 400
