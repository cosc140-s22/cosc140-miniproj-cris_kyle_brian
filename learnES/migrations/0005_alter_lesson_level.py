# Generated by Django 4.0.4 on 2022-05-25 23:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnES', '0004_answer_grade_question_delete_achievement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]