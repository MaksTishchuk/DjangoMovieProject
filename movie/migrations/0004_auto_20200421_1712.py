# Generated by Django 3.0.5 on 2020-04-21 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200420_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-id'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
    ]
