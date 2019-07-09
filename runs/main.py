import os
import time
import falcon
from apscheduler.schedulers.background import BackgroundScheduler

from runs.serve import Index
from runs.runs import Run

start = Run()
interval = os.environ.get('SCHEDULER_INTERVAL', 60)


def tasks():
    # Enable tasks for alerta service
    start.run_alerta()

scheduler = BackgroundScheduler()

scheduler.add_job(tasks, 'interval', minutes=int(interval), id='tasks')
scheduler.start()

app = falcon.API()
app.add_route('/', Index())
