from django.db import models


class Developer:
    pass


class Manager:
    pass


class Task(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    status = models.IntegerField(default='1')
    priority = models.IntegerField(default='1')

    def __str__(self):
        return self.name

