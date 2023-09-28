FROM python:3.11.5-bookworm

RUN mkdir /server && apt-get update && apt-get install -y git libpq-dev postgresql-client
WORKDIR /server

COPY ./ /server

RUN pip install poetry && poetry config virtualenvs.create false && poetry install
RUN chmod +x /server/worker-entrypoint.sh
