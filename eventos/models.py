from django.contrib.gis.db import models

# Create your models here.

class Tipo(models.Model):
  nome = models.CharField(max_length=200)
  desc = models.TextField()
  icon = models.CharField(max_length=100)

  def __unicode__(self):
    return "%s" % self.nome


class Evento(models.Model):
  tipo = models.ForeignKey(Tipo)
  titulo = models.CharField(max_length=200)
  posicao = models.PointField()
  objects = models.GeoManager()
  data = models.DateTimeField()

  def __unicode__(self):
    return self.titulo

  class Meta:
    ordering = ["-data", "titulo"]

class Vitima(models.Model):
  nome = models.CharField(max_length=200, blank=True, null=True)
  idade = models.IntegerField(blank=True, null=True)
  evento = models.ForeignKey(Evento)

  def __unicode__(self):
    return "%s (%i) - %s" % (self.nome, self.idade, self.evento)

class Registro(models.Model):
  evento = models.ForeignKey(Evento)
  link = models.URLField()

  def __unicode__(self):
    return self.link


class Bairro(models.Model):
  nome = models.CharField(max_length=200)
  mpoly = models.MultiPolygonField()
  objects = models.GeoManager()

  def __unicode__(self):
    return self.nome


class Pais(models.Model):
  nome = models.CharField(max_length=200)
  rate = models.DecimalField(max_digits = 5, decimal_places=2 )
  continente = models.CharField(max_length=200)

  def __unicode__(self):
    return self.nome

  class Meta:
    ordering = ['continente', 'nome']
