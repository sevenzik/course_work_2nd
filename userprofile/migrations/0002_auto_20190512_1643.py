# Generated by Django 2.1.4 on 2019-05-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='test_started',
            field=models.BooleanField(default=False),
        ),
    ]
