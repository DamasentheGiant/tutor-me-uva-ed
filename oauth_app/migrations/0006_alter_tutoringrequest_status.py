# Generated by Django 4.1.7 on 2023-04-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_app', '0005_tutoringrequest_status_alter_tutoringrequest_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoringrequest',
            name='status',
            field=models.BooleanField(default=None, null=True),
        ),
    ]