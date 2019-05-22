import os
import celery
import logging

from runs.services.alerta import AlertaClient
from runs.utils import Execute
from runs.exceptions import TaskExceptions

# Move these variables to a global file
CELERY_BROKER = os.environ.get('CELERY_BROKER', 'redis://localhost:6379/0')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND', 'redis://localhost:6379/0')

app = celery.Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)

execute = Execute()


@app.task()
def send_events_alerta(name, command, event, service, environment,
                       text, data, **status_event):

    alerta = AlertaClient()
    executed = execute.cmd(command)

    event_data = {
            'resource': name,
            'event': event,
            'environment': environment,
            'service': service,
            'text': text,
            'data': data
        }

    status = status_event.get('status')

    try:
        if executed and '0' in executed or 'OK' in executed:
            if 'success' in status[name]:
                event_data.update({
                        'severity': status[name]['success']['severity'],
                        'value': status[name]['success']['value']
                    })
        else:
            if 'fail' in status[name]:
                event_data.update({
                        'severity': status[name]['fail']['severity'],
                        'value': status[name]['fail']['value']
                    })
    except Exception as err:
        raise TaskExceptions({
                'Name': name,
                'Command': command,
                'Error': err
            })
    else:
        alerta.send_event(resource=event_data.get('resource'),
                          event=event_data.get('event'),
                          environment=event_data.get('environment'),
                          service=event_data.get('service'),
                          text=event_data.get('text'),
                          value=event_data.get('value'),
                          severity=event_data.get('severity'),
                          raw_data=event_data.get('data'))
    return executed


@app.task()
def only_execute(command):
    executed = execute.cmd(command)
    return executed
