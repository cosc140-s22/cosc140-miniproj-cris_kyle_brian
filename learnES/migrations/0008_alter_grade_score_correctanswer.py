# Generated by Django 4.0.4 on 2022-05-27 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learnES', '0007_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='score',
            field=models.IntegerField(default=0.0),
        ),
        migrations.CreateModel(
            name='CorrectAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learnES.answer')),
                ('question_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learnES.question')),
            ],
        ),
    ]
