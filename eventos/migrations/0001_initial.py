# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tipo'
        db.create_table(u'eventos_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'eventos', ['Tipo'])

        # Adding model 'Evento'
        db.create_table(u'eventos_evento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Tipo'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('posicao', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'eventos', ['Evento'])

        # Adding model 'Registro'
        db.create_table(u'eventos_registro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventos.Evento'])),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'eventos', ['Registro'])

        # Adding model 'Bairro'
        db.create_table(u'eventos_bairro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mpoly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'eventos', ['Bairro'])


    def backwards(self, orm):
        # Deleting model 'Tipo'
        db.delete_table(u'eventos_tipo')

        # Deleting model 'Evento'
        db.delete_table(u'eventos_evento')

        # Deleting model 'Registro'
        db.delete_table(u'eventos_registro')

        # Deleting model 'Bairro'
        db.delete_table(u'eventos_bairro')


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
        }
    }

    complete_apps = ['eventos']