# Generated by Django 4.0.4 on 2022-05-27 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnES', '0008_alter_grade_score_correctanswer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CorrectAnswer',
        ),
    ]
