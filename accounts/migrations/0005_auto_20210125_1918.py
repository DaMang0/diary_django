# Generated by Django 3.1 on 2021-01-25 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210123_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_name',
            field=models.CharField(default='anonymous', max_length=25),
        ),
    ]
