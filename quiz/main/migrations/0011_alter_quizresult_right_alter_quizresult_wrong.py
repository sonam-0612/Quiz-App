# Generated by Django 4.2.2 on 2023-08-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_quizresult_delete_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizresult',
            name='right',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quizresult',
            name='wrong',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
