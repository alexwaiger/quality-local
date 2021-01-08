# -*- coding: utf-8 -*-
from .models import Software, Country, Payment
from django.http import HttpResponse

def site_data(request):
    return {'countries': Country.objects.all(), 'providers': Software.objects.all(), 'payments': Payment.objects.all() }
    
def get_id(request, usr_id=0):
    if 'anid' in request.GET :
        usr_id = request.GET['anid']
        request.session["usr_id"] = usr_id
    elif 'usr_id' in request.session :
        usr_id = request.session.get('usr_id')
    else:
        usr_id = None
    return {'usr_id':usr_id, }