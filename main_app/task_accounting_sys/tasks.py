from .models import Task
from celery import shared_task
from datetime import timedelta
from datetime import datetime


@shared_task()
def delete_exp_task():
    string_of_tasks_names = ''
    queryset = Task.objects.filter(status='1_TO_DO')
    for obj in queryset:
        if (obj.create_date.replace(tzinfo=None) + timedelta(days=obj.life_time)) < datetime.now():
            string_of_tasks_names += (str(obj.name) + ', ')
            obj.delete()
    string_of_tasks_names = string_of_tasks_names.rstrip(', ')
    if len(string_of_tasks_names) == 0:
        message = 'No expired tasks'
    elif len(string_of_tasks_names) == 1:
        message = f'Task "{string_of_tasks_names}" has been deleted'
    else:
        message = f'Tasks "{string_of_tasks_names}" has been deleted'
    return message