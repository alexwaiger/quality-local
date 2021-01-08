# -*- coding: utf-8 -*-
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin
from .models import Casino, Payment, Software, Currency, Country, Games
from .translation import Casino, CasinoTranslationOptions

class CasinoAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'position', 'link', 'is_active')
    ordering = ('position',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class CountryAdmin(TabbedTranslationAdmin):
    list_display = ('name_en',)

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class GamesAdmin(TabbedTranslationAdmin):
    list_display = ('name',)

admin.site.register(Casino, CasinoAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Games, GamesAdmin)