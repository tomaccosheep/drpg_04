#!/bin/bash
python3 manage.py makemigrations
python3 manage.py makemigrations make_dj
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:9020
