#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
    while ! nc -z -v $KAFKA_URL; do
      sleep 3;
    done
    echo "PostgreSQL and Kafka started"
fi

python manage.py migrate
python manage.py collectstatic --no-input --clear

# Нужно будет настроить NGINX для работы со статикой
#gunicorn config.wsgi:application --bind 0.0.0.0:8000
exec "$@"