#!/bin/sh
# export C_FORCE_ROOT=1
python manage.py migrate smartmap
python manage.py runserver 0.0.0.0:8000
