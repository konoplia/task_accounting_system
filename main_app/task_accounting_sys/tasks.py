from .models import Task
from celery import shared_task
from datetime import timedelta
from datetime import datetime


@shared_task
def delete_exp_task():
    queryset = Task.objects.filter(status=1)
    for obj in queryset:
        if obj.create_date.replace(tzinfo=None) + timedelta(days=obj.life_time) > datetime.now():
            obj.delete()
    return len(queryset)
