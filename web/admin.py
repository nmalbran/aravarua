from django.contrib import admin
from web.models import *


admin.site.register(Categoria)


class UnidadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'slug')

admin.site.register(Unidad, UnidadAdmin)


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'unidad', 'publicada', 'creada', 'modificada', 'creada_por', 'modificada_por')
    exclude = ('creada_por', 'modificada_por')

admin.site.register(Noticia, NoticiaAdmin)


class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'archivo', 'publicado', 'unidad', 'categoria', 'creado', 'modificado', 'creado_por', 'modificado_por')
    exclude = ('creado_por', 'modificado_por')

admin.site.register(Recurso, RecursoAdmin)
