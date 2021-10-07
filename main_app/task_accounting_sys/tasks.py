from celery import shared_task
from .models import Task
from celery.schedules import crontab
from celery import shared_task
from datetime import timedelta
from datetime import datetime
# from celery.utils.log import get_task_logger
#
#
# logger = get_task_logger(__name__)


@shared_task
def delete_exp_task():
    queryset = Task.objects.all()
    for obj in queryset:
        if obj.create_date.replace(tzinfo=None) + timedelta(days=1) < \
                datetime.now() and int(obj.status) == 1:
            obj.delete()

