#!/bin/bash
python3 /app/replacer.py
python3 /app/manage.py makemigrations
python3 /app/manage.py makemigrations make_dj
python3 /app/manage.py migrate
python3 /app/manage.py runserver 0.0.0.0:80
