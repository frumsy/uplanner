# Generated by Django 2.0.2 on 2018-04-23 12:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0033_schedulecourse_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='uid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
    ]