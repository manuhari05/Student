# Generated by Django 5.1.2 on 2024-10-22 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_remove_student_classteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='performance',
            field=models.FloatField(default=0.0),
        ),
    ]