# Generated by Django 3.2.13 on 2022-10-07 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='desactivate_at',
            new_name='deactivate_at',
        ),
    ]
