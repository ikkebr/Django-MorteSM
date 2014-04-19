from django.shortcuts import render
from models import *

POP = 300000/100000.0

def rate():
  import datetime
  hoje = datetime.datetime.now()
  inicio = datetime.datetime(day=1, year=2014, month=1)
  dias = (hoje-inicio).days+1.0
  mortes = Vitima.objects.all().count()
  
  extrapolado = mortes/dias * 365

  rate = extrapolado/POP

  return (rate, extrapolado, mortes, dias)


def home(request):
  eventos = Evento.objects.all()
  #print eventos[0].posicao.tuple[:]
  taxa = rate()

  from django.db.models import Q
  maiores = Q(rate__gte=taxa[0])
  menores = Q(rate__lte=taxa[0])

  paises_maiores = Pais.objects.filter(maiores).order_by('rate')
  paises_menores = Pais.objects.filter(menores).order_by('-rate')

  paises_menores = paises_menores[::-1]
  return render(request, "mapa.html", locals())
