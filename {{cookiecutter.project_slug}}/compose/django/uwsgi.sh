#!/bin/sh

python /app/manage.py collectstatic --noinput
uwsgi --ini /app/config/uwsgi.ini