# Generated by Django 2.0.2 on 2018-04-23 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0042_auto_20180423_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
    ]