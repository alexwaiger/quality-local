# Generated by Django 3.1.1 on 2020-11-13 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0012_auto_20201113_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casino',
            name='adv1_au',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='adv2_au',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='adv3_au',
        ),
    ]
