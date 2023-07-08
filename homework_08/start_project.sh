#!/bin/bash

docker compose up -d
docker compose -f docker-compose_rabbit.yml up -d

cd pro_platform

python manage.py migrate
python manage.py runserver