# runs

Execute, take the output of any script file or command and send it to different web services.

When I can use this tool:

* I execute script(s) file(s) or command(s) as task(s) (schedule task(s) as well)
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

Contributions are always welcome. Please fork the repo, create a pull request against master, and be sure tests pass. See the [GitHub Flow](https://guides.github.com/introduction/flow/) for details.

## Authors

* [Marius Stanca](mailto:me@marius.xyz)
