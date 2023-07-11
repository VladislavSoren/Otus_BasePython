#!/bin/bash

docker compose up -d

sleep 15
cd pro_platform

poetry install
python manage.py migrate
python manage.py runserver