# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from .models import Casino, Country, Games

class CasinoTranslationOptions(TranslationOptions):
    fields = ('review', 'seo_title', 'seo_description', )
    
class GamesTranslationOptions(TranslationOptions):
    fields = ('name', 'seo_title', 'seo_description', )
    
class CountryTranslationOptions(TranslationOptions):
    fields = ('name', 'adj_name','menu_name', 'text', 'top_text', 'seo_title', 'seo_description', )
    
translator.register(Casino, CasinoTranslationOptions)
translator.register(Games, GamesTranslationOptions)
translator.register(Country, CountryTranslationOptions)