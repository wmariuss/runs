#!/bin/bash

gunicorn --reload -b 0.0.0.0:8000 runs.main:app --timeout 90 --log-level info
