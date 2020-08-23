import os
import sys
import site
site.addsitedir('/home/pi/Desktop/django_labo/djangoenv/lib/python3.7/site-packages')

import sys
sys.path.append('/home/pi/Desktop/django_labo/django_school/django_school')


sys.path.append('/home/pi/Desktop/django_labo/django_school')


from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_school.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_school.settings'

application = get_wsgi_application()
