#!/bin/bash
until nc -z -v -w30 db 3306
do
  echo "Waiting for database connection..."
  # wait for 5 seconds before check again
  sleep 5
done
echo "coucou"

python manage.py makemigrations && python manage.py makemigrations blog && python manage.py migrate 
gunicorn VulgaireDev.wsgi -b 0.0.0.0:8000 
