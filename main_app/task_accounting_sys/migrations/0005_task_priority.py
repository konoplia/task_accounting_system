# Generated by Django 3.2.7 on 2021-09-23 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_accounting_sys', '0004_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(1, 'High'), (2, 'Med'), (3, 'Low')], default='1'),
        ),
    ]
