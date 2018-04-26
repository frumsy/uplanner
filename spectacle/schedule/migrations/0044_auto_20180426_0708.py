# Generated by Django 2.0.2 on 2018-04-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0043_remove_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='session',
            field=models.CharField(blank=True, choices=[('un', 'University'), ('uc', 'University Eligible/CPE'), ('ud', 'University Non-standard Dates'), ('ce', 'CPE Continuing Education'), ('cu', 'CPE Non-Standard Dates'), ('c1', 'CPE Summer Session 1'), ('c2', 'CPE Summer Session 2'), ('c3', 'CPE Summer Session 3')], default='u', help_text='The course career', max_length=2),
        ),
    ]
