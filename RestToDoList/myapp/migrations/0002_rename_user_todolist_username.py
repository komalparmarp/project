# Generated by Django 4.0.1 on 2022-02-07 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='user',
            new_name='username',
        ),
    ]
