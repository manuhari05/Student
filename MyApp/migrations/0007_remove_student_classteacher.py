# Generated by Django 5.1.2 on 2024-10-22 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_student_teacher_id_alter_teacher_empid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classteacher',
        ),
    ]