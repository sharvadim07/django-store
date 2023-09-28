#!/bin/sh

until cd /server/store
do
    echo "Waiting for server volume..."
done


# until python manage.py migrate
# do
#     echo "Waiting for db to be ready..."
#     sleep 2
# done


python manage.py collectstatic --noinput

# First start
# python manage.py createsuperuser --noinput

gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# For debug
#python manage.py runserver 0.0.0.0:8000
