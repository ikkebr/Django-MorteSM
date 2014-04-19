from django.contrib.gis import admin
from models import *
from django.contrib.gis.geos import GEOSGeometry


class RegistroInline(admin.StackedInline):
  model = Registro

class VitimaInline(admin.StackedInline):
  model = Vitima

class GooAdmin(admin.OSMGeoAdmin):
 g = GEOSGeometry('POINT (-53.804 -29.684)')

 g.set_srid(4326) 
 g.transform(900913) 

 default_lon = int(g.x) 
 default_lat = int(g.y) 

 default_zoom = 11

 inlines = [VitimaInline, RegistroInline, ]


admin.site.register(Bairro, admin.GeoModelAdmin)
admin.site.register(Evento, GooAdmin)
admin.site.register(Tipo)
admin.site.register(Registro)
admin.site.register(Pais)
