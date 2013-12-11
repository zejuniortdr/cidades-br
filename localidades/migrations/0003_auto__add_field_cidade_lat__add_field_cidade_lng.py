# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cidade.lat'
        db.add_column('localidades_cidade', 'lat',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cidade.lng'
        db.add_column('localidades_cidade', 'lng',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cidade.lat'
        db.delete_column('localidades_cidade', 'lat')

        # Deleting field 'Cidade.lng'
        db.delete_column('localidades_cidade', 'lng')


    models = {
        'localidades.cidade': {
            'Meta': {'ordering': "('uf', 'nome')", 'object_name': 'Cidade'},
            'area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
            'codigo_ibge': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'densidade_demografica': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localidades.Estado']"}),
            'gentilico': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pib': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'populacao': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'localidades.estado': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Estado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['localidades']