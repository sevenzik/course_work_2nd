# Generated by Django 2.1.4 on 2019-05-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_auto_20190511_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='donetest',
            name='numberOfRightAnswers',
            field=models.BigIntegerField(default=0),
        ),
    ]
