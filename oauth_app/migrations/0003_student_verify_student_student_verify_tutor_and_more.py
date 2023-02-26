# Generated by Django 4.1.7 on 2023-02-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_app', '0002_remove_student_email_remove_tutor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='verify_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='verify_tutor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutor',
            name='verify_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutor',
            name='verify_tutor',
            field=models.BooleanField(default=False),
        ),
    ]