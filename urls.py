import os.path
from django.conf.urls.defaults import patterns, include, url

from django.views.generic.simple import direct_to_template


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

ROOT = os.path.dirname(__file__)

css_folder = os.path.join(ROOT, 'css')
js_folder = os.path.join(ROOT, 'js')

def build_full_path(folder):
    """Because django.views.static.serve expects a absolute/full path!"""
    return os.path.join(ROOT, folder)


urlpatterns = patterns('',
    url(r'^$', 'homepage.views.index', name='index'),

    #  http://fredericiana.com/2010/06/09/three-ways-to-add-a-robots-txt-to-your-django-project/
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),

    # pg.52 in Learning Website Development with Django
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': build_full_path('css')}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': build_full_path('js')}),
    (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': build_full_path('img')}),

    # from https://docs.djangoproject.com/en/1.2/howto/static-files/
    (r'^stuff/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': build_full_path('stuff') }),

    # TODO serve it from nginx!
    url(r'^blog/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': build_full_path('blog/build/html'),
        'show_indexes': True
    }),
)
