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
	list_display = ('nome', 'estado',)
	list_filter = ['estado',]
	save_on_top = True

admin.site.register(Cidade, CidadeAdmin)