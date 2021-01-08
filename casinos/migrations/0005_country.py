# Generated by Django 3.1.1 on 2020-11-05 13:45

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0004_auto_20201030_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.CharField(max_length=50, verbose_name='url')),
                ('flag', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='upload/img/flags/', verbose_name='flag')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
