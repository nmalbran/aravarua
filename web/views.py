from django.views.generic import DetailView, ListView, View
# from django.shortcuts import render_to_response, redirect, get_object_or_404
# from django.http import HttpResponse, Http404
# from django.template import RequestContext

from web.models import Noticia, Unidad, Recurso


class NoticiaListView(ListView):
    model = Noticia
    template_name = 'info/noticias.html'
    context_object_name = 'noticias'
    paginate_by = 7

    def get_queryset(self):
        return super(NoticiaListView, self).get_queryset().filter(unidad__slug=self.kwargs['slug'], publicada=True).order_by('-creada')


class RecursoListView(ListView):
    model = Recurso
    template_name = 'info/recursos.html'
    context_object_name = 'recursos'
    paginate_by = 20

    def get_queryset(self):
        return super(RecursoListView, self).get_queryset().filter(unidad__slug=self.kwargs['slug'], publicado=True).order_by('categoria', '-creado')
