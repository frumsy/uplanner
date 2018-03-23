# Generated by Django 2.0.2 on 2018-03-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_section_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='gened',
            field=models.ManyToManyField(blank=True, help_text='Enter any gened categories this course satisfies', to='schedule.Gened'),
        ),
        migrations.AlterField(
            model_name='course',
            name='reqs',
            field=models.TextField(blank=True, default='', help_text='Enter the course requirements', max_length=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(blank=True, help_text='The previous courses taken by the user', to='schedule.Section'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
