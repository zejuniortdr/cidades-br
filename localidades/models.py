# coding: utf-8
from django.db import models

# Create your models here.

class Estado(models.Model):
	"""(Estado description)"""
	uf = models.CharField(max_length=2)
	nome = models.CharField(max_length=255)


	class Meta:
		verbose_name, verbose_name_plural = u"Estado" , u"Estados"
		ordering = ('nome',)

	def __unicode__(self):
		return "%s" % self.nome


class Cidade(models.Model):
	"""(Cidade description)"""
	estado = models.ForeignKey(Estado)
	uf = models.CharField(max_length=2,verbose_name=u'UF')
	nome = models.CharField(max_length=255)
	codigo_ibge = models.IntegerField(null=True,blank=True)
	gentilico = models.CharField(max_length=255, verbose_name=u'Gentílico',null=True,blank=True)
	populacao = models.IntegerField(verbose_name=u'População em 2010',null=True,blank=True)
	area = models.DecimalField(verbose_name=u'Área da unidade territorial (km²)',max_digits=11, decimal_places=2,null=True,blank=True)
	densidade_demografica = models.DecimalField(verbose_name=u"Densidade demográfica (hab/km²)", max_digits=11, decimal_places=2,null=True,blank=True)
	pib = models.IntegerField(verbose_name="PIB",null=True,blank=True)


	class Meta:
		verbose_name, verbose_name_plural = u"Cidade" , u"Cidades"
		ordering = ('uf','nome',)

	def __unicode__(self):
		return "%s" % self.nome
