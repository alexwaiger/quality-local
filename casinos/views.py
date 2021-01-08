# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import render, redirect
import random
import os
import numpy as np
from django.http import Http404
from django.db.models import Count

from .models import Casino, Software, Country

from django.views.decorators.cache import never_cache


def home(request):
    casino_list = Casino.objects.filter(is_active=True).order_by('-trust_score', 'position')
    context = {'objects': casino_list }
    return render(request, 'home.html', context)

def contacts(request):
    return render(request, 'contacts.html')
    
def about(request):
    return render(request, 'about.html')
    
def privacy(request):
    return render(request, 'privacy.html')
    
def black_list(request):
    return render(request, 'black-list.html')
    
def sitemap(request):
    casino_list = Casino.objects.filter(is_active=True).order_by('-trust_score', 'position')
    context = {'casinos': casino_list, }
    return render(request, 'sitemap.html', context)

def countries(request, slug):
    slug = slug
    try:
        country = Country.objects.get(slug=slug)
        casino_list = Casino.objects.filter(is_active=True, country=country).order_by('-trust_score', 'position')
        context = {'objects': casino_list, 'country': country }
    except:
        raise Http404()
    return render(request, 'home.html', context)

def bonuses(request, slug=0):
    slug = slug
    if slug == 0 :
        try:
            casino_list = Casino.objects.filter(is_active=True).order_by('-bonus_score', '-bonus', '-limit', 'position')
            context = {'objects': casino_list, }
        except:
            raise Http404()
    else:
        try:
            country = Country.objects.get(slug=slug)
            casino_list = Casino.objects.filter(is_active=True, country=country).order_by('-bonus_score', '-bonus', '-limit', 'position')
            context = {'objects': casino_list, 'country': country }
        except:
            raise Http404()
    return render(request, 'bonuses.html', context)

def payouts(request, slug=0):
    slug = slug
    if slug == 0 :
        try:
            casino_list = Casino.objects.filter(is_active=True).annotate(count=Count('pay')).order_by('-support_score', '-count', 'position')
            context = {'objects': casino_list, }
        except:
            raise Http404()    
    else:
        try:
            country = Country.objects.get(slug=slug)
            casino_list = Casino.objects.filter(is_active=True, country=country).annotate(count=Count('pay')).order_by('-support_score', '-count', 'position')
            context = {'objects': casino_list, 'country': country }
        except:
            raise Http404()
    return render(request, 'payments.html', context)

def games(request, slug=0):
    slug = slug
    if slug == 0 :
        try:
            casino_list = Casino.objects.filter(is_active=True).annotate(count=Count('soft')).order_by('-games_score', '-games', '-count', 'position')
            context = {'objects': casino_list, }
        except:
            raise Http404()    
    else:
        try:
            country = Country.objects.get(slug=slug)
            casino_list = Casino.objects.filter(is_active=True, country=country).annotate(count=Count('soft')).order_by('-games_score', '-games', '-count', 'position')
            context = {'objects': casino_list, 'country': country }
        except:
            raise Http404()
    return render(request, 'games.html', context)

def reviews(request):
    try:
        casino_list = Casino.objects.filter(is_active=True).order_by('-trust_score', 'position')
        context = {'objects': casino_list, }
    except:
        raise Http404()
    return render(request, 'reviews.html', context)

def review(request, slug=0):
    slug = slug
    if slug == slug.lower() :
        if slug == 0 :
            raise Http404()
        else:
            try:
                casino = Casino.objects.get(name__iexact=slug)
                context = {'object': casino, }
            except:
                raise Http404()
        return render(request, 'review.html', context)
    else:
        url = '/'+request.LANGUAGE_CODE+'/reviews/'+slug.lower()+'/'
        return redirect(url, permanent=True)