# Generated by Django 3.2.7 on 2021-10-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_accounting_sys', '0003_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('1', 'TO DO'), ('2', 'READY'), ('3', 'IN PROGRESS'), ('4', 'COMPLETED')], default='1', max_length=1),
        ),
    ]
