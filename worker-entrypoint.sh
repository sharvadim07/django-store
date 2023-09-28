#!/bin/sh

until cd /server/store
do
    echo "Waiting for server volume..."
done

# run a worker
celery -A store worker --loglevel=info --concurrency 1 -E
