# Generated by Django 2.2 on 2021-01-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0031_auto_20210106_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='casino',
            name='review_ru',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Review'),
        ),
        migrations.AddField(
            model_name='casino',
            name='seo_description_ru',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='casino',
            name='seo_title_ru',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='country',
            name='adj_name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='adjective name'),
        ),
        migrations.AddField(
            model_name='country',
            name='menu_name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='menu'),
        ),
        migrations.AddField(
            model_name='country',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='country',
            name='seo_description_ru',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='country',
            name='seo_title_ru',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='country',
            name='text_ru',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Page text'),
        ),
        migrations.AddField(
            model_name='country',
            name='top_text_ru',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Top page text'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_ru',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_ru',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
    ]
