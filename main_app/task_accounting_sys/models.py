from django.db import models
# from main_app.authentication.models import NewUser
from main_app.main_app.settings import AUTH_USER_MODEL

User = AUTH_USER_MODEL


class Developer(NewUser):
    pass
    # class Meta:


class Manager(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    #     model = NewUser
    # pass

    def __str__(self):
        return self.user.user_name


class Task(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    status = models.IntegerField(default='1')
    priority = models.IntegerField(default='1')
    created_by = models.ForeignKey('Manager', on_delete=models.CASCADE, null=True)
    # created_by = models.IntegerField(id=request.user.id)

    def __str__(self):
        return self.name

