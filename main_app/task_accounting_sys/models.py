from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('1_TO_DO', 'TO_DO'),
    ('2_READY', 'READY'),
    ('3_IN_PROGRESS', 'IN_PROGRESS'),
    ('4_COMPLETED', 'COMPLETED'),
)

PRIORITY_CHOICES = (
    ('3_LOW', 'LOW'),
    ('2_NORMAL', 'NORMAL'),
    ('1_HIGH', 'HIGH'),
)


class Task(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='1_TO_DO')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='1_HIGH')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='creator_tasks', null=True)
    executor = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='executor_tasks', null=True)
    life_time = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

