#!/usr/bin/env bash

python manage.py collectstatic --noinput && \
python manage.py migrate --noinput && \
uwsgi --strict --ini uwsgi.ini
