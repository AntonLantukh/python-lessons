#!/usr/bin/env bash

echo "Run migrations"

DJANGO_SUPERUSER_PASSWORD=12345
DJANGO_SUPERUSER_USERNAME=admin

python manage.py makemigrations
python manage.py migrate
python manage.py createadmin 

echo "Done migrations"

exec "$@"

echo "Starting app"

uwsgi --ini uwsgi.ini
