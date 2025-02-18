# Используем официальный Python 3.13 (slim — минимальный образ)
FROM python:3.13-slim

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    TZ=Asia/Bishkek

# Определяем рабочую директорию
WORKDIR /usr/src/app

# Устанавливаем зависимости системы
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Копируем зависимости и устанавливаем их
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Открываем порт 8000 для Django
EXPOSE 8000

# Запускаем сервер через Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
