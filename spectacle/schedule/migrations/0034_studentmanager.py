# Generated by Django 2.0.2 on 2018-04-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0033_auto_20180410_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
