# Generated by Django 3.1.1 on 2020-12-22 07:40

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0023_casino_ads_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casino',
            name='review_pl',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='review_ru',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='seo_description_pl',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='seo_description_ru',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='seo_title_pl',
        ),
        migrations.RemoveField(
            model_name='casino',
            name='seo_title_ru',
        ),
        migrations.RemoveField(
            model_name='country',
            name='menu_name_pl',
        ),
        migrations.RemoveField(
            model_name='country',
            name='menu_name_ru',
        ),
        migrations.RemoveField(
            model_name='country',
            name='seo_description_pl',
        ),
        migrations.RemoveField(
            model_name='country',
            name='seo_description_ru',
        ),
        migrations.RemoveField(
            model_name='country',
            name='seo_title_pl',
        ),
        migrations.RemoveField(
            model_name='country',
            name='seo_title_ru',
        ),
        migrations.RemoveField(
            model_name='country',
            name='text_pl',
        ),
        migrations.RemoveField(
            model_name='country',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='games',
            name='name_pl',
        ),
        migrations.RemoveField(
            model_name='games',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='games',
            name='seo_description_pl',
        ),
        migrations.RemoveField(
            model_name='games',
            name='seo_description_ru',
        ),
        migrations.RemoveField(
            model_name='games',
            name='seo_title_pl',
        ),
        migrations.RemoveField(
            model_name='games',
            name='seo_title_ru',
        ),
        migrations.AddField(
            model_name='country',
            name='adj_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='adjective name'),
        ),
        migrations.AddField(
            model_name='country',
            name='logo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='upload/img/flags/', verbose_name='flag for page'),
        ),
    ]