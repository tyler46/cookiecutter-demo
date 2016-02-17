import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def path(*x):
    return os.path.join(BASE_DIR, *x)


DEBUG = config('DEBUG', cast=bool)
BIND = config('BIND')
PORT = config('PORT', cast=int)

{% if cookiecutter.use_db == 'y' -%}
DATABASE_URL = config('DATABASE_URL')
{%- endif %}

{% if cookiecutter.expose_api == 'n' -%}
TEMPLATE_DIRS = config('TEMPLATE_DIRS', default=path('templates'))
{%- endif %}
