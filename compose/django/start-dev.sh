#!/bin/sh
pip install --user -r requirements.txt
#python manage.py migrate
python manage.py runserver 0:8000