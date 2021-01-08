import os, sys
sys.path.append('/home/boss/www/django/quality')
os.environ['DJANGO_SETTINGS_MODULE'] = 'quality.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()