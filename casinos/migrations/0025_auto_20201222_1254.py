# Generated by Django 3.1.1 on 2020-12-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0024_auto_20201222_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='adj_name',
            field=models.CharField(max_length=50, verbose_name='adjective name'),
        ),
    ]