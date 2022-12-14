#!/bin/bash
echo "Start backend server"
until cd /app/pymango
do
    echo "Waiting for server volume..."
done

until python3 manage.py migrate
do
    echo "Waiting for database to be ready..."
    sleep 2
done
python3 manage.py makemigrations
python3 manage.py collectstatic --noinput

gunicorn pymango.wsgi --preload --bind 0.0.0.0:8000 --workers 4 --threads 4