# Generated by Django 3.1 on 2021-02-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gratitude', '0002_gratitude_list_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gratitude_list',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
