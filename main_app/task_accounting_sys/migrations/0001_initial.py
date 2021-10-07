# Generated by Django 3.2.7 on 2021-10-07 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[(1, 'TO DO'), (2, 'READY'), (3, 'IN PROGRESS'), (4, 'COMPLETED')], default=1, max_length=30)),
                ('priority', models.IntegerField(default='1')),
                ('executor', models.IntegerField()),
                ('created_by', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
