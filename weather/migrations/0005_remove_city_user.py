# Generated by Django 2.1.7 on 2019-03-13 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_city_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='user',
        ),
    ]
