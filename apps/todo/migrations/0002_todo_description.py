# Generated by Django 3.2.13 on 2022-09-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=1, verbose_name='Descrição'),
            preserve_default=False,
        ),
    ]
