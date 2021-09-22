from django.db import models


class Task(models.Model):

    TASK_STATUS = (
                      (1, 'TODO'), (2, 'READY'), (3, 'IN PROGRESS'),
                      (4, 'COMPLETED')
    )

    PRIORITY = (
        (1, 'High'), (2, 'Med'), (3, 'Low')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TASK_STATUS, default='1')
    priority = models.IntegerField(choices=PRIORITY)

    def __str__(self):
        return self.name
