import os 
import sys

sys.path.append('/home/dlam/hg/dlam_me')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# vi: ft=python
