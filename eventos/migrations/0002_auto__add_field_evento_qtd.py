# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Evento.qtd'
        db.add_column(u'eventos_evento', 'qtd',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Evento.qtd'
        db.delete_column(u'eventos_evento', 'qtd')


    models = {
        u'eventos.bairro': {
            'Meta': {'object_name': 'Bairro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'eventos.evento': {
            'Meta': {'ordering': "['-data', 'titulo']", 'object_name': 'Evento'},
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posicao': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'qtd': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Tipo']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'eventos.registro': {
            'Meta': {'object_name': 'Registro'},
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Evento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'eventos.tipo': {
            'Meta': {'object_name': 'Tipo'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['eventos']