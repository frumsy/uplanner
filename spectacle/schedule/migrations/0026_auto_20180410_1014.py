# Generated by Django 2.0.2 on 2018-04-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0025_auto_20180410_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AddField(
            model_name='student',
            name='credits',
            field=models.IntegerField(default=0, help_text='The current cumulative number of credits taken'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sid',
            field=models.CharField(default='', help_text='8 digit spire id', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
