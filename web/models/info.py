from django.db import models
from django.utils.translation import ugettext_lazy as _


class Unidad(models.Model):
    nombre = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _('Unidad')
        verbose_name_plural = _('Unidades')
        app_label = 'web'

    def __unicode__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)

    unidad = models.ForeignKey('Unidad')

    publicada = models.BooleanField(default=True)
    creada = models.DateTimeField(auto_now_add=True, editable=False)
    modificada = models.DateTimeField(auto_now=True, editable=False)

    creada_por = models.ForeignKey('auth.User', related_name='noticias_creadas', null=True, default=True)
    modificada_por = models.ForeignKey('auth.User', related_name='noticias_modificadas', null=True, default=True)

    class Meta:
        verbose_name = _('Noticia')
        verbose_name_plural = _('Noticias')
        app_label = 'web'

    def __unicode__(self):
        return "%s (%s)" % (self.titulo, self.creada)


class Recurso(models.Model):
    unidad = models.ForeignKey('Unidad')
    nombre = models.CharField(max_length=100)
    archivo = models.CharField(max_length=255)
    categoria = models.ForeignKey('Categoria')

    publicado = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True, editable=False)
    modificado = models.DateTimeField(auto_now=True, editable=False)

    creado_por = models.ForeignKey('auth.User', related_name='recursos_creados', null=True, default=True)
    modificado_por = models.ForeignKey('auth.User', related_name='recursos_modificados', null=True, default=True)

    class Meta:
        verbose_name = _('Recurso')
        verbose_name_plural = _('Recursos')
        app_label = 'web'

    def __unicode__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')
        app_label = 'web'

    def __unicode__(self):
        return self.nombre

