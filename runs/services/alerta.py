import os
import logging
from alertaclient.api import Client


class AlertaClient(object):
    def __init__(self):
        default_url = "http://localhost:8080/api"

        self.endpoint = os.environ.get("ALERTA_ENDPOINT", default_url)
        self.key = os.environ.get("ALERTA_KEY", "")
        self.ssl_verify = os.environ.get("ALERTA_SSL_VERIFY", False)

        self.client = Client(
            endpoint=self.endpoint, key=self.key, ssl_verify=self.ssl_verify
        )

    def send_event(self, **event_params):
        """
        Object constructor expects nine arguments.

        :param resource: resource under alarm, deliberately not host-centric
        :param event: event name eg. NodeDown
        :param environment: effected environment, development, \
            staging or production
        :param service: list of effected services
        :param text: freeform text description
        :param value: event value eg. 100%, Down, PingFail, 55ms, ORA-1664
        :param severity: severity of alert (default normal)
        :param timeout: number of seconds before alert is considered stale
        :param raw_data: log event or the steps to resolve
        """
        if len(event_params) >= 8:
            try:
                self.client.send_alert(
                    resource=event_params.get("resource"),
                    event=event_params.get("event"),
                    environment=event_params.get("environment"),
                    service=event_params.get("service", None),
                    text=event_params.get("text"),
                    value=event_params.get("value"),
                    severity=event_params.get("severity"),
                    timeout=event_params.get("timeout", 86400),
                    raw_data=event_params.get("raw_data"),
                )
            except Exception:
                logging.error("Could not send events to alerta service", exc_info=True)
