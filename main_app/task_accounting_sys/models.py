from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (1, 'TO DO'),
    (2, 'READY'),
    (3, 'IN PROGRESS'),
    (4, 'COMPLETED')
)

PRIORITY = [
    (1, "HIGH"),
    (2, "NORMAL"),
    (3, "LOW"),

]


class Task(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default='1')
    priority = models.IntegerField(choices=PRIORITY, default='1')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                   auto_created=True)
    executor = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

