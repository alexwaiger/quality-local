# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from .models import Casino, Country
from django.urls import reverse

class StaticHomeSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'
    protocol = "https"
    i18n = True

    def items(self):
        return ['home', ]

    def location(self, item):
        return reverse(item)

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'
    protocol = "https"
    i18n = True

    def items(self):
        return ['privacy', 'contacts', 'about', 'sitemap', 'black_list', 'reviews' ]

    def location(self, item):
        return reverse(item)

class CasinoSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"
    i18n = True

    def items(self):
        return Casino.objects.filter(is_active=True)

    def location(self, obj):
        return reverse('review', args=[obj.name.lower()])

class CountrySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"
    i18n = True

    def items(self):
        return Country.objects.all()

    def location(self, obj):
        return reverse('countries', args=[obj.slug])