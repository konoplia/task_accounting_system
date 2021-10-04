from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (1, 'TO DO'),
    (2, 'READY'),
    (3, 'IN PROGRESS'),
    (4, 'COMPLETED')
)


class Task(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    # status = models.CharField(max_length=50, choices=STATUS, default='1')
    status = models.CharField(max_length=50, choices=STATUS, default='TODO')
    priority = models.IntegerField(default='1')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                   auto_created=True)
    executor = models.IntegerField()

    def __str__(self):
        return self.name

