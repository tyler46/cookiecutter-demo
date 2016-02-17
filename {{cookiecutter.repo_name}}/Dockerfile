FROM python:2.7-slim

MAINTAINER {{ cookiecutter.author_name }}

CMD ["./bin/run.sh"]

EXPOSE 8080

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential libpq-dev netcat postgresql-client python-dev python-pip && \
    apt-get autoclean -y && \
    rm -f /var/cache/apt/archives/*.deb && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install gunicorn
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app
