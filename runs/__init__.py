import os
import logging
import urllib3


logging.basicConfig(
    filename="/var/log/runs.log",
    format="%(asctime)s - %(levelname)s, %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO"),
)

logging.getLogger(__name__)

urllib3.disable_warnings()
