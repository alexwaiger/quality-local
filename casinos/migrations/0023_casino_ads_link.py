# Generated by Django 3.1.1 on 2020-12-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0022_auto_20201209_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='ads_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ads Link'),
        ),
    ]
