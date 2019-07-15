#!/bin/bash

set -e

echo "Runing worker..."
# concurrency=4 : number of child processes processing the queue
# purge : purges all waiting tasks before the daemon is started
# autoscale=10,3 : enable autoscaling by providing max_concurrency,min_concurrency

STAGE=$1

if [ $# -eq 0 ]; then
    echo "Please give an argument to continue the script. Eg. local or docker."
else
    if [ "$STAGE" == "local" ]; then
        celery worker -A runs.tasks --autoscale=10,3 --purge --loglevel=INFO
    elif [ "$STAGE" == "docker" ]; then
       celery worker -A runs.tasks --purge --loglevel=INFO
    fi
fi
