from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


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

