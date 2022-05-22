#!/bin/bash
pip3 install --user -r requirements.txt
#python manage.py migrate
python3 manage.py check --deploy
python3 manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 snumap.wsgi:application
