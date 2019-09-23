# runs

[![Build Status](https://travis-ci.com/wmariuss/runs.svg?branch=master)](https://travis-ci.com/wmariuss/runs)
[![Tag](https://img.shields.io/github/v/tag/wmariuss/runs)](https://github.com/wmariuss/runs/tags)
[![License](https://img.shields.io/github/license/wmariuss/runs)](https://github.com/wmariuss/runs/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Execute any script file or command as job and send the result to different web services.

When I can use this tool:

* I execute script file(s) or command(s) as task(s) (schedule task(s) as well)
* I send the output to different web services
* I want all tasks to be executed in parallel

## Services

Check [docs](docs/) dir for available services.

## Requirements

* `Python >= 3.6`
* Depends of the service you want to use you need `endpoint` and `token`
* `redis >= 4.0.9`

## Install

Local

* `pip install pipenv`
* `pipenv install`

Docker

* `docker-compose build`

## Usage

Local

* Copy `env.example` to `.env`
* `pipenv run bash start.sh local`
* `pipenv run bash worker.sh local`

Docker

* Copy `env.docker.example` to `.env.docker`
* `docker-compose up -d`

## Tests

Soon.

## Contribute

Contributions are always welcome.

* Fork the repo
* Create a pull request against master
* Be sure tests pass (if exists)

Check [GitHub Flow](https://guides.github.com/introduction/flow/) for details.

## Authors

* [Marius Stanca](mailto:me@marius.xyz)
