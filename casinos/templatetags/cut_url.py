# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter
from casinos.models import Casino

register = template.Library()

@register.filter
@stringfilter
def get_nonlang_url(value):
    if value == '/':
        new_url = value[1:]
    else:
        new_url = value[4:]
    return new_url
    
@register.filter
@stringfilter
def lower(value):
    return value.lower()
    
@register.filter
@stringfilter
def aff(value, usr_id=None):
    object = Casino.objects.get(id=value)
    seo_link = object.link
    ads_link = object.ads_link
    if usr_id and ads_link :
        if 'atraff' in ads_link :
            link = ads_link + '&anid=' + usr_id + '#registration'
        elif 'boomerang' in ads_link :
            link = ads_link + '&anid=' + usr_id
        elif 'toponepartners' in ads_link :
            link = ads_link + '?s2s.req_id=' + usr_id
        elif 'media' in ads_link :
            link = ads_link + '&clickid=' + usr_id
        else :
            link = ads_link
    else:
        link = seo_link
    return link

@register.filter
@stringfilter
def refilter(value, country):
    list = value
    return list