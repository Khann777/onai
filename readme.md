# 🚀 Webhook API with LLM Processing

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Django](https://img.shields.io/badge/Django-5.1-green.svg)
![Celery](https://img.shields.io/badge/Celery-5.4-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-✅-blue.svg)
![FastAPI](https://img.shields.io/badge/Pydantic-✅-red.svg)

## 📖 Описание проекта
Этот проект реализует **REST API-сервис** для обработки **webhook-запросов** с помощью **LLM (GPT, Claude, LLaMA)** и асинхронной обработки задач через **Celery**.

📌 **Функционал проекта:**
- 📡 Прием Webhook-запросов (`/webhook/`)
- 🤖 Интеграция с LLM (через OpenAI API или OpenRouter)
- 🔄 Асинхронная обработка запросов через Celery
- 🔗 Отправка результата на callback URL
- 📝 Валидация входных данных через **Pydantic**
- 📑 Авто-документация API с помощью **Swagger**
- 🚀 Использование **PostgreSQL** + **Redis** + **Docker**
- 📊 Логирование событий и ошибок
- 🛠️ Тестирование через **pytest**

---

## 🚀 **1. Установка**
### 📌 **1.1. Клонируем репозиторий**
```bash
git clone https://github.com/your-repo/webhook-llm.git
cd webhook-llm
```

📌 1.2. Устанавливаем зависимости
```
pip install -r requirements.txt
```
📌 1.3. Создаем .env файл

Создай .env файл в корне проекта и добавь в него:

```
SECRET_KEY=
DEBUG=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

REDIS_URL=

OPENROUTER_API_KEY=
```
🏗️ 2. Запуск проекта

📌 2.1. Запуск базы данных
```
docker-compose up -d
```

После запуска сервер доступен по адресу:

📌 http://127.0.0.1:8000/


📌 3.1. Отправка webhook-запроса
POST /webhook/
📌 Пример запроса:
```
{
  "message": "Привет, бот!",
  "callback_url": "https://example.com/callback"
}
```
📌 Пример ответа:
```
{
  "message": "Accepted"
}
```
📑 4. Документация API

Swagger-документация доступна по адресу:

📌 http://127.0.0.1:8000/swagger/

🧪 5. Тестирование

Запуск всех тестов:
```
pytest
```
Запуск тестов с отчетом:
```
pytest -v --tb=short
```
🛠️ 6. Технологии

Проект использует:

Django Rest Framework (API)

Pydantic (валидация данных)

Celery + Redis (асинхронная обработка)

PostgreSQL (база данных)

pytest (тестирование)



