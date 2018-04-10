# Generated by Django 2.0.2 on 2018-04-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0013_schedulecourse_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='career',
            field=models.CharField(blank=True, choices=[('u', 'Undergraduate'), ('g', 'Graduate'), ('c', 'Non-Credit'), ('d', 'Non-Degree')], default='u', help_text='The course career', max_length=1),
        ),
    ]