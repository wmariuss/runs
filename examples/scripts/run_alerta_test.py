import os
import requests
from alertaclient.api import Client

urls_list = {"Development": "https://ifconfig.co", "Staging": "https://ifconfig.co"}

client = Client(
    endpoint=os.environ["ALERTA_ENDPOINT"], key=os.environ["ALERTA_KEY"], ssl_verify=False
)

info = {
    "environment": "Production",
    "service": ["WebApp"],
    "text": "Check HTTP status code",
}

for stage in urls_list:
    if stage == "Development":
        status = requests.get(str(urls_list.get(stage)))
        info.update({"environment": stage})

    if stage == "Staging":
        status = requests.get(str(urls_list.get(stage)))
        info.update({"environment": stage})

    if status.status_code != 200:
        info.update(
            {
                "value": str(status.status_code),
                "severity": "citical",
                "data": "Check https://ifconfig.co/",
            }
        )
    else:
        info.update(
            {
                "value": str(status.status_code),
                "severity": "normal",
                "data": "You do not have to do anything",
            }
        )

    send = client.send_alert(
        resource="Ping",
        event="StatusCode",
        environment=info.get("environment"),
        service=info.get("service"),
        text=info.get("text"),
        value=info.get("value"),
        severity=info.get("severity"),
        raw_data=info.get("data"),
    )

    print(send)
