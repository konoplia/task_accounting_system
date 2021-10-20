from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

STATUS = (
    (1, _('TO DO')),
    (2, _('READY')),
    (3, _('IN PROGRESS')),
    (4, _('COMPLETED'))
)

# PRIORITY = [
#     (1, "HIGH"),
#     (2, "NORMAL"),
#     (3, "LOW"),

# ]

LOW = 3
NORMAL = 2
HIGH = 1
PRIORITY_CHOICES = (
    (LOW, 'Low'),
    (NORMAL, 'Normal'),
    (HIGH, 'High'),
)


class Task(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)
    priority = models.CharField(max_length=200, choices=PRIORITY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                   auto_created=True, blank=True, null=True)
    executor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
