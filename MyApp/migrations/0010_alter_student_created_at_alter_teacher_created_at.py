# Generated by Django 5.1.2 on 2024-10-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_student_created_at_student_updated_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]