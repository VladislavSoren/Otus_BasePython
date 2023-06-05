# FROM python:3.9-buster
FROM python:3.10

# Флаг, чтобы не использовалась буферизация логов (в докере не оч корректно работает)
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
workdir /app

# Обновляем pip и ставим pipenv
run pip install --upgrade pip
run pip install "pipenv==2023.6.2"

# Копируем файлы зависимостей в рабочую директорию
copy Pipfile Pipfile.lock ./

# Устанавливаем pipenv в систему (OS), без создания venv
run pipenv install --system  --ignore-pipfile

# Переносим весь код в рабочую директорию контейнера
COPY blog .

# Запускаем uvicorn сервер на заданном хосте и порту
# uvicorn main:app --host 0.0.0.0 --port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Указываем что внешний порт это 8000
EXPOSE 8000

# "uvicorn main:app --host 0.0.0.0 --port 8000"

