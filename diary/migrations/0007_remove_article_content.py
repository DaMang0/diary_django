# Generated by Django 3.1 on 2021-02-02 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_auto_20210202_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
    ]
