from django.contrib import admin
from web.models import *


class UnidadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'slug')

admin.site.register(Unidad, UnidadAdmin)


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'unidad', 'publicada', 'creada', 'modificada', 'creada_por', 'modificada_por')
    exclude = ('creada_por', 'modificada_por')

admin.site.register(Noticia, NoticiaAdmin)
