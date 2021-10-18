from .models import Task
from celery import shared_task
from datetime import timedelta
from datetime import datetime


@shared_task
def delete_exp_task():
    queryset = Task.objects.all()
    for obj in queryset:
        if obj.create_date.replace(tzinfo=None) + timedelta(days=1) < \
                datetime.now() and int(obj.status) == 1:
            obj.delete()
