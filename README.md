# runs

Execute any script file or command as job and send the result to different web services.

When I can use this tool:

* I execute script file(s) or command(s) as task(s) (schedule task(s) as well)
* I send the output to different web services
* I want all tasks to be executed in parallel

## Services

* [x] Alerta (monitoring and alerting)
* [ ] More soon

## Requirements

* `Python >= 3.6`
* Depends of the service you want to use you need `endpoint` and `token`
* `redis >= 4.0.9`

## Install

Development

* `pip install pipenv`
* `pipenv install --dev`
* `pipenv run bash start.sh`

## Usage

Currently this is `beta` stage.

* Create new `.env` file (example [here](env.template))
* `pipenv run bash start.sh`
* `pipenv run bash worker.sh`

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
