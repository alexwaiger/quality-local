# Generated by Django 3.1.1 on 2020-10-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0003_auto_20201030_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='logo_color',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='Logo color'),
        ),
    ]
