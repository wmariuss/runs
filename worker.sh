#!/bin/bash

echo "Runing worker..."
# concurrency=4 : number of child processes processing the queue
# purge : purges all waiting tasks before the daemon is started
# autoscale=10,3 : enable autoscaling by providing max_concurrency,min_concurrency

celery worker -A runs.tasks --autoscale=10,3 --purge --loglevel=INFO
