# Generated by Django 3.1.1 on 2020-11-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0008_auto_20201111_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='country',
            field=models.ManyToManyField(blank=True, related_name='country', to='casinos.Country'),
        ),
    ]
