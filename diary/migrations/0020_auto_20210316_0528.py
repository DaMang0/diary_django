# Generated by Django 3.1 on 2021-03-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0019_auto_20210311_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('1', 'Article'), ('2', 'Creativity'), ('3', 'Diary'), ('4', 'Journal'), ('5', 'Knowledge')], default='1', max_length=25, unique=True),
        ),
    ]