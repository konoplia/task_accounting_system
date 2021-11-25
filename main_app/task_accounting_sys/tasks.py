from .models import Task
from django.core.mail import send_mail
from celery import shared_task
from datetime import timedelta
from datetime import datetime


@shared_task
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


# @shared_task
# def send_mail_to_executor(user_email, task_name):
#     name = f'You have new task: {task_name}'
#     mail = send_mail('New task', message=name, from_email='djangotest313@gmail.com', recipient_list=[user_email])
#     return mail
@shared_task
def send_mail_to_executor(task_id):
    task = Task.objects.get(id=task_id)
    name = f'You have new task: {task.name}'
    mail = send_mail('New task', message=name, from_email='djangotest313@gmail.com', recipient_list=[task.executor.email])
    return mail