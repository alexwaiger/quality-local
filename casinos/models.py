# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from django.utils.safestring import mark_safe

from datetime import datetime, timedelta
import random

CHOICES = (
    ('50', '5.0'),
    ('49', '4.9'),
    ('48', '4.8'),
    ('47', '4.7'),
    ('46', '4.6'),
    ('45', '4.5'),
    ('44', '4.4'),
    ('43', '4.3'),
    ('42', '4.2'),
    ('41', '4.1'),
    ('40', '4.0'),
    ('35', '3.5'),
    ('30', '3.0'),
    ('25', '2.5'),
    ('20', '2.0'),
    ('15', '1.5'),
    ('10', '1.0'),
    ('0', '0.0'),
)

QUALITY_CHOICES = (
    ('new', 'Newest'),
    ('best', 'Best'),
    ('win', 'Winner'),
)

class Payment(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo for black bg', upload_to="upload/img/pay/", blank=False)
    logo_inverted = ThumbnailerImageField(u'logo for white bg', upload_to="upload/img/pay/", blank=True, null=True)
    prioritet = models.IntegerField(u'Prioritet', default=0)
    seo_title = models.TextField(u'SEO Title', max_length=80, blank=True, null=True)
    seo_description = models.TextField(u'SEO Description', max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-prioritet', ]
        verbose_name  = u"Payment"
        verbose_name_plural  = u"Payments"
        
class Games(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo for black bg', upload_to="upload/img/games/", blank=True)
    logo_inverted = ThumbnailerImageField(u'logo for white bg', upload_to="upload/img/games/", blank=True)
    prioritet = models.IntegerField(u'Prioritet', default=0)
    seo_title = models.TextField(u'SEO Title', max_length=80, blank=True, null=True)
    seo_description = models.TextField(u'SEO Description', max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-prioritet', ]
        verbose_name  = u"Games"
        verbose_name_plural  = u"Games"
        
class Country(models.Model):
    name =  models.CharField(u'name', max_length=50)
    menu_name =  models.CharField(u'menu', max_length=50)
    adj_name =  models.CharField(u'adjective name', max_length=50)
    slug =  models.CharField(u'url', max_length=50)
    prioritet = models.IntegerField(u'Prioritet', default=0)
    logo = ThumbnailerImageField(u'flag for page', upload_to="upload/img/flags/page/", blank=True)
    flag = ThumbnailerImageField(u'flag', upload_to="upload/img/flags/", blank=True)
    top_text = models.TextField(u'Top page text', max_length=300, blank=True, null=True)
    text = models.TextField(u'Quality text', max_length=10000, blank=True, null=True)
    bonus_text = models.TextField(u'Bonus text', max_length=10000, blank=True, null=True)
    payout_text = models.TextField(u'Payout text', max_length=10000, blank=True, null=True)
    games_text = models.TextField(u'Games text', max_length=10000, blank=True, null=True)
    seo_title = models.TextField(u'SEO Title', max_length=80, blank=True, null=True)
    seo_description = models.TextField(u'SEO Description', max_length=200, blank=True, null=True)
    
    
    def __str__(self):
        return self.name
        
    def safetext(self):
        if self.text:
            if '<script>' in self.text:
                self.is_malicious = True
                self.save()
                return self.text
        else:
            return None
        return mark_safe(self.text)
        
    def safetoptext(self):
        if self.top_text:
            if '<script>' in self.top_text:
                self.is_malicious = True
                self.save()
                return self.top_text
        else:
            return None
        return mark_safe(self.top_text)
    
    class Meta:
        ordering = ['-prioritet', ]
        verbose_name  = u"Country"
        verbose_name_plural  = u"Countries"
        
class Software(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo for black bg', upload_to="upload/img/soft/", blank=False)
    logo_inverted = ThumbnailerImageField(u'logo for white bg', upload_to="upload/img/soft/", blank=True, null=True)
    prioritet = models.IntegerField(u'Prioritet', default=0)
    seo_title = models.TextField(u'SEO Title', max_length=80, blank=True, null=True)
    seo_description = models.TextField(u'SEO Description', max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-prioritet', ]
        verbose_name  = u"Software"
        verbose_name_plural  = u"Softwares"
        
class Currency(models.Model):
    name =  models.CharField(u'name', max_length=50)
    logo = ThumbnailerImageField(u'logo', upload_to="upload/img/currency/", blank=True)
    prioritet = models.IntegerField(u'Prioritet', default=0)
    seo_title = models.TextField(u'SEO Title', max_length=80, blank=True, null=True)
    seo_description = models.TextField(u'SEO Description', max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-prioritet', ]
        verbose_name  = u"Currency"
        verbose_name_plural  = u"Currencies"

class Casino(models.Model):
    is_active = models.BooleanField(u'Is Active', default=True, blank=False, null=False)
    name =  models.CharField(u'Title', max_length=50)
    position = models.IntegerField(u'Position')
    link = models.URLField(u'Link', max_length=200)
    bonus_link = models.URLField(u'Bonus Link', max_length=200, blank=True, null=True)
    ads_link = models.URLField(u'Ads Link', max_length=200, blank=True, null=True)
    logo_color = models.CharField(u'Logo color', max_length=7, blank=True, null=True)
    trust_score = models.CharField(u'Trust & Fairness Score', max_length=3, choices=CHOICES)
    games_score = models.CharField(u'Games & Software Score', max_length=3, choices=CHOICES)
    bonus_score = models.CharField(u'Bonuses & Promo Score', max_length=3, choices=CHOICES)
    support_score = models.CharField(u'Payment & Withdraw Score', max_length=3, choices=CHOICES)
    logo = ThumbnailerImageField(u'Casino Logo', upload_to="upload/img/logos/")
    image = ThumbnailerImageField(u'Gif Image', upload_to="upload/img/gifs/")
    badge = models.CharField(u'Badge', max_length=8, choices=QUALITY_CHOICES, blank=True, null=True)
    currency = models.ManyToManyField(Currency, blank=False)
    soft = models.ManyToManyField(Software, blank=False)
    pay = models.ManyToManyField(Payment, related_name='pays', blank=False)
    withdraw = models.ManyToManyField(Payment, related_name='payout', blank=False)
    country = models.ManyToManyField(Country, related_name='country', blank=True)
    game_types = models.ManyToManyField(Games, related_name='gametype', blank=True)
    games = models.IntegerField(u'Games count', blank=True, null=True)
    bonus = models.IntegerField(u'Welcome bonus', blank=False, null=False)
    fs = models.IntegerField(u'Free Spins', default=0, blank=False, null=False)
    limit = models.IntegerField(u'Bonus limit', null=True)
    deposit = models.IntegerField(u'Min Deposit', blank=True, null=True)
    mobile = models.BooleanField(u'Mobile', blank=True, null=True)
    live = models.BooleanField(u'Live chat', blank=True, null=True)
    fun = models.BooleanField(u'Free games', blank=True, null=True)
    license = models.URLField(u'License', max_length=500, blank=True, null=True)
    twitter = models.URLField(u'Twitter', max_length=200, blank=True, null=True)
    fb = models.URLField(u'FaceBook', max_length=200, blank=True, null=True)
    instagram = models.URLField(u'Instagram', max_length=200, blank=True, null=True)
    email = models.EmailField(u'Support E-mail', max_length=256, blank=True, null=True)
    phone = models.CharField(u'Support Phone', max_length=20, blank=True, null=True)
    winner = models.URLField(u'WinLink', max_length=200, blank=True, null=True)
    ankor = models.CharField(u'Anchor', max_length=50, blank=True, null=True)
    review = models.TextField(u'Review', max_length=5000, blank=True, null=True)
    review_bonuses = models.TextField(u'Review bonuses', max_length=5000, blank=True, null=True)
    review_countries = models.TextField(u'Review countries', max_length=5000, blank=True, null=True)
    review_currencies = models.TextField(u'Review currencies', max_length=5000, blank=True, null=True)
    review_providers = models.TextField(u'Review providers', max_length=5000, blank=True, null=True)
    review_payments = models.TextField(u'Review payments', max_length=5000, blank=True, null=True)
    review_games = models.TextField(u'Review games', max_length=5000, blank=True, null=True)
    review_info = models.TextField(u'Review info', max_length=5000, blank=True, null=True)
    seo_title = models.TextField(u'SEO Title', max_length=80, blank=True, null=True)
    seo_description = models.TextField(u'SEO Description', max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name

    @property
    def rating(self):
        trust = (int(self.trust_score))*2
        games = (int(self.games_score))*2
        bonus = (int(self.bonus_score))*2
        support = (int(self.support_score))*2
        rating = (float(trust+games+bonus+support))/4
        return rating
        
    def review_date(self):
        pos = self.position
        days = pos + 20
        revdate = datetime.now() - timedelta(days=days)
        return revdate
        
    class Meta:
        ordering = ['-trust_score',]
        verbose_name  = u"Casino"
        verbose_name_plural  = u"Casinos"