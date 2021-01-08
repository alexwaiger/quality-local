# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from casinos import views
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView

from django.views.static import serve
from django.conf import settings

from casinos.models import Casino
from django.contrib.sitemaps.views import sitemap
from casinos.sitemap import StaticHomeSitemap, StaticViewSitemap, CasinoSitemap, CountrySitemap

sitemaps = {
    'home': StaticHomeSitemap,
    'static': StaticViewSitemap,
    'casino': CasinoSitemap,
    'countries': CountrySitemap,
}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps, 'template_name': 'xml-sitemap.xml'},
     name='django.contrib.sitemaps.views.sitemap'),
]
urlpatterns += [
    url(r'send/$', RedirectView.as_view(url='/', permanent = True )),
    url(r'search/$', RedirectView.as_view(url='/', permanent = True )),
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    ]

urlpatterns += i18n_patterns(
    url(r'en/$', RedirectView.as_view(url='/', permanent = True )),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path( r'admin/', admin.site.urls),
    path(r'', views.home, name='home'),
    prefix_default_language = False
)
urlpatterns += i18n_patterns(
    path(r'about/', views.about, name='about'),
    path(r'contacts/', views.contacts, name='contacts'),
    path(r'privacy/', views.privacy, name='privacy'),
    path(r'sitemap/', views.sitemap, name='sitemap'),
)
urlpatterns += i18n_patterns(
    path(r'best-bonuses/', views.bonuses, name='bonuses'),
    path(r'best-payouts/', views.payouts, name='payouts'),
    path(r'best-games/', views.games, name='games'),
    path(r'black-list/', views.black_list, name='black_list'),
    path(r'reviews/', views.reviews, name='reviews'),
    path(r'reviews/<slug:slug>/', views.review, name='review'),
    path(r'<slug:slug>/', views.countries, name='countries'),
    path(r'<slug:slug>/best-bonuses/', views.bonuses, name='bonuses'),
    path(r'<slug:slug>/best-payouts/', views.payouts, name='payouts'),
    path(r'<slug:slug>/best-games/', views.games, name='games'),
)