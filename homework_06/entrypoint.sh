#!/usr/bin/env bash

echo "Run migrations"

flask db upgrade

echo "Done migrations"

exec "$@"

echo "Starting app"

gunicorn -c gunicorn.conf.py
