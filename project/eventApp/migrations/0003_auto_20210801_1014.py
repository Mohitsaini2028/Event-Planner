# Generated by Django 3.1.6 on 2021-08-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0002_auto_20210731_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(),
        ),
    ]
