# coding: utf-8
from django import forms
from django.contrib import admin
from models import *

class EstadoAdmin(admin.ModelAdmin):
	search_fields = ('nome', 'uf',)
	list_display = ('nome', 'uf',)
	save_on_top = True

admin.site.register(Estado, EstadoAdmin)

class CidadeAdmin(admin.ModelAdmin):
	search_fields = ('nome', 'uf',)
	list_display = ('nome', 'estado','lat','lng','capital')
	list_filter = ['estado','capital',]
	readonly_fields = ('estado','uf','nome','codigo_ibge','gentilico','populacao','area','densidade_demografica','pib','lat','lng','capital',)
	#list_editable = ('capital',)
	save_on_top = True

	fieldsets = [
		('Cidade',{'fields': ['nome','capital',], 'classes': ['wide']}),
		(u'Estado',{'fields': ['estado', 'uf',], 'classes': ['wide']}),
		(u'Informacções IBGE',{'fields': ['codigo_ibge','gentilico','populacao','area','densidade_demografica','pib',], 'classes': ['wide']}),
		(u'Coordenadas Google Maps',{'fields': ['lat','lng',], 'classes': ['wide']}),
	]

admin.site.register(Cidade, CidadeAdmin)
