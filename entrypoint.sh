#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn fitweb.wsgi:application --bind 178.16.128.64:8000
