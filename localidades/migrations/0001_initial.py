# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estado'
        db.create_table('localidades_estado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('localidades', ['Estado'])

        # Adding model 'Cidade'
        db.create_table('localidades_cidade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localidades.Estado'])),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('localidades', ['Cidade'])


    def backwards(self, orm):
        # Deleting model 'Estado'
        db.delete_table('localidades_estado')

        # Deleting model 'Cidade'
        db.delete_table('localidades_cidade')


    models = {
        'localidades.cidade': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Cidade'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localidades.Estado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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