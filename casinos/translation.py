# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import Casino, Country, Games

class CasinoTranslationOptions(TranslationOptions):
    fields = ('phone', 'review', 'review_bonuses', 'review_countries', 'review_currencies', 'review_providers', 'review_payments', 'review_games', 'review_info', 'seo_title', 'seo_description', )
    
class GamesTranslationOptions(TranslationOptions):
    fields = ('name', 'seo_title', 'seo_description', )
    
class CountryTranslationOptions(TranslationOptions):
    fields = ('name', 'adj_name','menu_name', 'text', 'bonus_text', 'payout_text', 'games_text', 'top_text', 'seo_title', 'seo_description', )
    
translator.register(Casino, CasinoTranslationOptions)
translator.register(Games, GamesTranslationOptions)
translator.register(Country, CountryTranslationOptions)