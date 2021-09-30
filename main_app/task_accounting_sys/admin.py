from django.contrib import admin
from .models import Task, Manager, Developer

# Register your models here.

admin.site.register(Task)
admin.site.register(Manager)
admin.site.register(Developer)
