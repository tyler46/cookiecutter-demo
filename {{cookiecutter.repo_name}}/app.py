{%- if cookiecutter.expose_api == 'y' -%}
import json
{%- endif %}
from bottle import (
    default_app, error, {% if cookiecutter.expose_api == 'n' %}HTTPError,{% endif %} response, run, {% if cookiecutter.expose_api == 'n' %}template, TEMPLATE_PATH{% endif %}
)
{% if cookiecutter.use_db == 'y' %}
from bottle.ext import sqlalchemy as sqlaplugin

import models
{%- endif %}
import settings


app = default_app()

{% if cookiecutter.use_db == 'y' %}
db_plugin = sqlaplugin.SQLAlchemyPlugin(models.engine, models.Base.metadata,
                                        create=True)
app.install(db_plugin)
{% endif %}
{% if cookiecutter.expose_api == 'n' -%}
TEMPLATE_PATH.append(settings.TEMPLATE_DIRS)
{%- endif %}

{% if cookiecutter.use_db == 'y' %}
@app.get('/:name')
def view(name, db):
    entity = db.query(models.Entity).filter_by(name=name).first()
    if entity:
        {% if cookiecutter.expose_api == 'y' -%}
        return {'id': entity.id, 'name': entity.name}
        {% else %}
        data = {
            'id': entity.id,
            'name': entity.name
        }
        return template('entity', data)
        {% endif %}

    {% if cookiecutter.expose_api == 'y' %}
    response.content_type = 'application/json'
    response.status = 410
    response.body = json.dumps({'message': 'entity not found'})
    return response
    {% else -%}
    return HTTPError(404, 'Entity not found.')
    {%- endif %}


@app.post('/:name')
def create(name, db):
    entity = models.Entity(name)
    db.add(entity)

    {% if cookiecutter.expose_api == 'y' -%}
    response.content_type = 'application/json'
    response.status = 201
    return response
    {% else -%}
    return 'CREATED'
    {%- endif %}
{% endif %}
{%- if cookiecutter.expose_api == 'y' %}
@app.get('/')
def index():
    return json.dumps({'message': 'Built something'})

@error(404)
def error404(error):
    return json.dumps({'error': 'nothing to see'})

{%- endif %}

if __name__ == '__main__':
    run(host=settings.BIND, port=settings.PORT, debug=settings.DEBUG)
else:
    application = app
