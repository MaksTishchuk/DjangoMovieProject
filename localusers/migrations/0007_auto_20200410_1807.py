# Generated by Django 3.0.5 on 2020-04-10 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localusers', '0006_auto_20200410_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localuser',
            name='created',
        ),
        migrations.RemoveField(
            model_name='localuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='localuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='localuser',
            name='location',
        ),
        migrations.RemoveField(
            model_name='localuser',
            name='modified',
        ),
    ]