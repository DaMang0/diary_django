# Generated by Django 3.1 on 2021-03-11 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0011_auto_20210311_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='article',
        ),
    ]