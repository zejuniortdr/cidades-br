# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cidade.codigo_ibge'
        db.add_column('localidades_cidade', 'codigo_ibge',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cidade.gentilico'
        db.add_column('localidades_cidade', 'gentilico',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cidade.populacao'
        db.add_column('localidades_cidade', 'populacao',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cidade.area'
        db.add_column('localidades_cidade', 'area',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Cidade.densidade_demografica'
        db.add_column('localidades_cidade', 'densidade_demografica',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Cidade.pib'
        db.add_column('localidades_cidade', 'pib',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cidade.codigo_ibge'
        db.delete_column('localidades_cidade', 'codigo_ibge')

        # Deleting field 'Cidade.gentilico'
        db.delete_column('localidades_cidade', 'gentilico')

        # Deleting field 'Cidade.populacao'
        db.delete_column('localidades_cidade', 'populacao')

        # Deleting field 'Cidade.area'
        db.delete_column('localidades_cidade', 'area')

        # Deleting field 'Cidade.densidade_demografica'
        db.delete_column('localidades_cidade', 'densidade_demografica')

        # Deleting field 'Cidade.pib'
        db.delete_column('localidades_cidade', 'pib')


    models = {
        'localidades.cidade': {
            'Meta': {'ordering': "('uf', 'nome')", 'object_name': 'Cidade'},
            'area': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
            'codigo_ibge': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'densidade_demografica': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localidades.Estado']"}),
            'gentilico': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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