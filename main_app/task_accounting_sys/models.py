from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    (1, 'TO_DO'),
    (2, 'READY'),
    (3, 'IN_PROGRESS'),
    (4, 'COMPLETED'),
)

PRIORITY_CHOICES = (
    (3, 'Low'),
    (2, 'Normal'),
    (1, 'High'),
)


class Task(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='creator_tasks', null=True)
    executor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='executor_tasks', null=True)
    life_time = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

