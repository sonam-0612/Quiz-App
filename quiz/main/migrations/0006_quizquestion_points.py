# Generated by Django 4.1.7 on 2023-07-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='points',
            field=models.IntegerField(default='2'),
        ),
    ]
