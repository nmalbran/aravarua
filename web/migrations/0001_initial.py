# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unidad'
        db.create_table('web_unidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('web', ['Unidad'])

        # Adding model 'Noticia'
        db.create_table('web_noticia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cuerpo', self.gf('django.db.models.fields.TextField')()),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Unidad'])),
            ('publicada', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('creada', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificada', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creada_por', self.gf('django.db.models.fields.related.ForeignKey')(default=True, related_name='noticias_creadas', null=True, to=orm['auth.User'])),
            ('modificada_por', self.gf('django.db.models.fields.related.ForeignKey')(default=True, related_name='noticias_modificadas', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('web', ['Noticia'])


    def backwards(self, orm):
        # Deleting model 'Unidad'
        db.delete_table('web_unidad')

        # Deleting model 'Noticia'
        db.delete_table('web_noticia')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'web.noticia': {
            'Meta': {'object_name': 'Noticia'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'creada': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creada_por': ('django.db.models.fields.related.ForeignKey', [], {'default': 'True', 'related_name': "'noticias_creadas'", 'null': 'True', 'to': "orm['auth.User']"}),
            'cuerpo': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificada': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modificada_por': ('django.db.models.fields.related.ForeignKey', [], {'default': 'True', 'related_name': "'noticias_modificadas'", 'null': 'True', 'to': "orm['auth.User']"}),
            'publicada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web.Unidad']"})
        },
        'web.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['web']