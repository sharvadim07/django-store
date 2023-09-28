FROM python:3.11.5-bookworm

RUN mkdir /server && apt-get update && apt-get install -y git libpq-dev postgresql-client
RUN pip install gunicorn
WORKDIR /server

COPY ./ /server

RUN chmod +x /server/worker-entrypoint.sh
RUN chmod +x /server/server-entrypoint.sh

RUN pip install poetry && poetry config virtualenvs.create false && poetry install
