# Generated by Django 3.1.1 on 2020-11-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0020_auto_20201117_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='name_au',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_de',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_en',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_fi',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_hu',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_it',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_nl',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_pl',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='name_sv',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_au',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_de',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_en',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_fi',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_hu',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_it',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_nl',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_pl',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_ru',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_description_sv',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_au',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_de',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_en',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_fi',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_hu',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_it',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_nl',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_pl',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_ru',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='games',
            name='seo_title_sv',
            field=models.TextField(blank=True, max_length=80, null=True, verbose_name='SEO Title'),
        ),
    ]
