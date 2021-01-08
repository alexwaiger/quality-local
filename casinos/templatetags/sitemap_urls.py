# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter
from casinos.models import Casino

from django.conf import settings

register = template.Library()

@register.filter
@stringfilter
def get_sitemap_url(value, lang):
    domain_name = settings.ALLOWED_HOSTS
    protocol = 'https://'
    domain = protocol + domain_name[0] + '/'
    refdomain = domain + 'en/'
    if value == domain:
        if lang == 'en':
            new_url = value
        else:
            new_url = value+lang+'/'
    else:
        dl = len(domain)+len(lang)
        new_url = domain + lang + value[dl:]
    if new_url == refdomain:
        new_url = domain
    return new_url