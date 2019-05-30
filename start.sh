#!/bin/bash

set -e

STAGE=$1

if [ $# -eq 0 ]; then
    echo "Please give an argument to continue the script. Eg. local or docker."
else
    if [ "$STAGE" == "local" ]; then
        gunicorn -b 0.0.0.0:8000 runs.main:app --timeout 90 --log-level info
    elif [ "$STAGE" == "docker" ]; then
        gunicorn -b 0.0.0.0:8000 runs.main:app --worker-tmp-dir /dev/shm --timeout 90 --log-level info
    fi
fi
