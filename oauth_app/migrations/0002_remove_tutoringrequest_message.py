# Generated by Django 4.1.7 on 2023-04-30 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutoringrequest',
            name='message',
        ),
    ]