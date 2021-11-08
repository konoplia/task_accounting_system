import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')

app = Celery('main_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-every-hour': {
        'task': 'task_accounting_sys.tasks.delete_exp_task',
        'schedule': crontab(minute=0, hour='*/1'),
    },
}
app.conf.timezone = "Europe/Kiev"

