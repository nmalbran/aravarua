from django.views.generic import DetailView, ListView, View
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext

from web.models import Noticia, Unidad


class NoticiaListView(ListView):
    model = Noticia
    template_name = 'info/noticias.html'

    def get_queryset(self):
        return super(NoticiaListView, self).get_queryset().filter(unidad__slug=self.kwargs['unidad_slug'])
