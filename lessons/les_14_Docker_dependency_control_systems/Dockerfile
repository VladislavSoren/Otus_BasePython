# FROM ubuntu
FROM python:3.10

# Флаг, чтобы не использовалась буферизация логов (в докере не оч корректно работает)
ENV PYTHONUNBUFFERED=1

workdir /app

run pip install --upgrade pip
run pip install "pipenv==2023.6.2"
copy Pipfile Pipfile.lock ./
# https://stackoverflow.com/questions/46503947/how-to-get-pipenv-running-in-docker
run pipenv install --system  --ignore-pipfile

COPY blog .

# Выполняется при старте (при входе в контейнер)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

# RUN apt update -y && apt upgrade -y && apt install -y python3.10