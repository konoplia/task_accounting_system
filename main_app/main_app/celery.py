import os

from celery import Celery
from celery.schedules import crontab

from .settings import FREQUENCY_START_FUNC

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')

app = Celery('main_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'check-every-12-hours': {
        'task': 'task_accounting_sys.tasks.delete_exp_task',
        'schedule': crontab(hour=FREQUENCY_START_FUNC),
    },
}
app.conf.timezone = 'UTC'
