from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to, direct_to_template

from views import NoticiaListView, RecursoListView

urlpatterns = patterns('',
    url(r'^/?$', redirect_to, {'url': '/noticias/aravarua'}),
    url(r'^nosotros/?$', direct_to_template, {'template': 'static/nosotros.html'}),
    url(r'^historia/?$', direct_to_template, {'template': 'static/historia.html'}),
    url(r'^unidades/?$', direct_to_template, {'template': 'static/unidades.html'}),
    url(r'^fotos/?$', direct_to_template, {'template': 'static/fotos.html'}),

    url(r'^noticias/(?P<slug>[-\w\d]+)/?$', NoticiaListView.as_view(), name='noticias_unidad'),
    url(r'^recursos/(?P<slug>[-\w\d]+)/?$', RecursoListView.as_view(), name='recursos_unidad'),

)