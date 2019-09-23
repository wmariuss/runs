import time

from runs.tasks import send_events_alerta
from runs.tasks import only_execute
from runs.load import Config


class Run(object):
    def __init__(self):
        pass

    def run_alerta(self):
        config = Config()
        data_config = config.get(service="alerta")
        status = {}

        for name, configs in data_config.items():
            if "general" != name:
                if "status" in configs:
                    status = {name: configs["status"]}

                send_events_alerta.delay(
                    name=name,
                    command=configs.get("run"),
                    event=configs.get("event"),
                    service=configs.get("service"),
                    environment=configs.get("environment"),
                    text=configs.get("text"),
                    data=configs.get("data"),
                    status=status,
                )
            else:
                for name in configs:
                    only_execute.delay(configs[name]["run"])
