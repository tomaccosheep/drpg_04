#!/bin/bash
python3 manage.py makemigrations user_app
python3 manage.py makemigrations 
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
