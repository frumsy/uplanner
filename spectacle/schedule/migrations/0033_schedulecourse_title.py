# Generated by Django 2.0.2 on 2018-04-23 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0032_auto_20180422_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulecourse',
            name='title',
            field=models.CharField(blank=True, default='', help_text='Enter the title of this event', max_length=50),
        ),
    ]