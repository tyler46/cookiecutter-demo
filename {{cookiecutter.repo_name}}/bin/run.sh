#!/bin/bash

{% if cookiecutter.use_db == 'y' %}
# assuming that running database container for web is named db
until nc -z db 5432; do
    echo "$(date) - waiting postgres container to get up ..."
    sleep 1
done
{% endif %}

gunicorn -b 0.0.0.0:8080 -w 3 --log-file debug --access-logfile wsgi:application
