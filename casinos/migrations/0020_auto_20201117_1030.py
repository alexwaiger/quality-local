# Generated by Django 3.1.1 on 2020-11-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0019_auto_20201117_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casino',
            name='games_count',
        ),
        migrations.AddField(
            model_name='casino',
            name='game_types',
            field=models.ManyToManyField(blank=True, related_name='gametype', to='casinos.Games'),
        ),
        migrations.RemoveField(
            model_name='casino',
            name='games',
        ),
        migrations.AddField(
            model_name='casino',
            name='games',
            field=models.IntegerField(blank=True, null=True, verbose_name='Games count'),
        ),
    ]
