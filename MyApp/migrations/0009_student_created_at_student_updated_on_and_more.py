# Generated by Django 5.1.2 on 2024-10-23 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_teacher_performance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 23, 5, 56, 14, 842268, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 23, 5, 56, 14, 842268, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='teacher',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]