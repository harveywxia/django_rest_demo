# Generated by Django 2.0.3 on 2018-11-05 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181105_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='pick_time',
        ),
    ]