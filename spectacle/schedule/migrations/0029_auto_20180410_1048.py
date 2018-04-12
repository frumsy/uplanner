# Generated by Django 2.0.2 on 2018-04-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0028_auto_20180410_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='student',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='student',
            name='major',
        ),
        migrations.RemoveField(
            model_name='student',
            name='sid',
        ),
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]