from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to, direct_to_template

from views import NoticiaListView

urlpatterns = patterns('',
    url(r'^/?$', redirect_to, {'url': '/noticias/aravarua'}),
    url(r'^nosotros/?$', direct_to_template, {'template': 'static/nosotros.html'}),
    url(r'^unidades/?$', direct_to_template, {'template': 'static/unidades.html'}),

    url(r'^noticias/(?P<slug>[-\w\d]+)/?$', NoticiaListView.as_view(), name='noticias_unidad'),

)