# Generated by Django 4.0.4 on 2022-05-25 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnES', '0005_alter_lesson_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='completion_percentage',
        ),
    ]
