# Generated by Django 3.1.6 on 2021-07-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='', upload_to='eventApp/images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(),
        ),
    ]