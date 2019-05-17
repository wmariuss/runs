# runs

Execute, take the output of any script file or command and send it to different web services.

When I can use this tool:

* I execute script(s) file(s) or command(s) as task(s) (schedule task(s) as well)
* I send the output to different web services
* I want all tasks to be executed in parallel

## Requirements

* `Python >= 3.6`
* Depends of the service you want to use you need `endpoint` and `token`
* `redis >= 4.0.9`

## Install

For easy deployment this is built as executable. You can download it from [release](https://github.com/wmariuss/runs/releases) section.

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

Very soon.

## Authors

* [Marius Stanca](mailto:me@marius.xyz)
