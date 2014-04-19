# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vitima'
        db.create_table(u'eventos_vitima', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('idade', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Evento'])),
        ))
        db.send_create_signal(u'eventos', ['Vitima'])

        # Deleting field 'Evento.quantidade'
        db.delete_column(u'eventos_evento', 'quantidade')


    def backwards(self, orm):
        # Deleting model 'Vitima'
        db.delete_table(u'eventos_vitima')

        # Adding field 'Evento.quantidade'
        db.add_column(u'eventos_evento', 'quantidade',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


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
        },
        u'eventos.vitima': {
            'Meta': {'object_name': 'Vitima'},
            'evento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eventos.Evento']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idade': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['eventos']