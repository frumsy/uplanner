# Generated by Django 2.0.2 on 2018-04-23 15:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0036_section_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='id',
        ),
        migrations.AlterField(
            model_name='section',
            name='sid',
            field=models.IntegerField(default=0, help_text='The 5 digit spire course number'),
        ),
        migrations.AlterField(
            model_name='section',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
