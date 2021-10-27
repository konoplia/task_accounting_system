from django.db import models
from django.contrib.auth.models import User


TO_DO = 1
READY = 2
IN_PROGRESS = 3
COMPLETED = 4
STATUS_CHOICES = (
    (TO_DO, 'TO_DO'),
    (READY, "READY"),
    (IN_PROGRESS, 'IN_PROGRESS'),
    (COMPLETED, 'COMPLETED')
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
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_tasks', blank=True)
    executor = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

