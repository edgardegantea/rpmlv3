from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import *
from .accionesAdmin import *



# Register your models here.
@admin.register(Informacion)
class InformacionAdmin(AdminResource, ExportarCsvMixin, admin.ModelAdmin):
    list_display = ('privacidad', 'nombre', 'nombreContro', 'telefono')
    # list_filter = ('nombre', 'nombreContro', 'telefono')
    ordering = ('privacidad', 'nombre', 'nombreContro', 'telefono')
    search_fields = ['nombre', 'nombreContro', 'telefono']
    list_per_page = 10
    empty_value_display = '-empty-'
    actions = ["exportar_a_csv"]


@admin.register(Area)
class AreaAdmin(AdminResource, admin.ModelAdmin):
    fields = [('clave', 'nombre'), 'ubicacion', ('latitud', 'longitud'),
              ('altitud', 'operando')]  # Organización de campos
    list_display = ('clave', 'nombre', 'Asentamiento', 'altitud', 'latitud', 'longitud', 'operando')
    # list_display_links = ('clave', 'nombre', 'ubicacion', 'altitud', 'latitud', 'operando')
    # list_filter = ('clave', 'nombre', 'ubicacion', 'operando')
    ordering = ('clave', 'nombre', 'Asentamiento', 'altitud', 'latitud', 'operando')
    search_fields = ['clave', 'nombre', 'Asentamiento', 'altitud', 'latitud', 'operando']
    list_per_page = 10
    empty_value_display = '-empty-'
    actions = ["exportar_a_csv"]


@admin.register(PlanDeContingencia)
class PlanDeContingenciaAdmin(AdminResource, admin.ModelAdmin):
    list_display = ('area', 'nombre', 'activo')
    # list_filter = ('area', 'nombre', 'activo')
    ordering = ('area', 'nombre', 'activo')
    search_fields = ['area', 'nombre', 'activo']
    list_per_page = 10
    empty_value_display = '-empty-'
    actions = ["exportar_a_csv"]


@admin.register(MonitorSequia)
class MonitorSequiaAdmin(AdminResource, admin.ModelAdmin):
    list_display = ('intensidad', 'descripcion')
    list_filter = ('intensidad', 'descripcion')
    ordering = ('intensidad', 'descripcion')
    search_fields = ['intensidad', 'descripcion']
    list_per_page = 10
    empty_value_display = '-empty-'
    actions = ["exportar_a_csv"]


@admin.register(Cultivos)
class CultivosAdmin(AdminResource, admin.ModelAdmin):
    # list_filter = ('nombre', 'nombreCientifico', 'descripcion', 'mesDeSiembra')
    list_display = ('imagen', 'nombre', 'nombreCientifico', 'descripcion', 'mesDeSiembra')
    list_per_page = 3
    ordering = ('nombre',)
    search_fields = ['nombre', 'nombreCientifico', 'descripcion', 'mesDeSiembra']
    actions = ["exportar_a_csv"]

    def imagen(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.imagenes.url,
            width='100px',
            height='100px',
        )
        )


@admin.register(CensoTemperatura)
class CensoTemperaturaAdmin(AdminResource, admin.ModelAdmin):
    list_display = ('Area', 'Cultivo', 'temperatura1', 'temperatura2', 'created_at')
    ordering = ('Area', 'Cultivo', 'temperatura1', 'temperatura2', 'created_at')
    search_fields = ['Area', 'Cultivo', 'temperatura1', 'temperatura2', 'created_at']
    # list_filter = ('Area', 'Cultivo')
    list_per_page = 10
    empty_value_display = '-empty-'
    actions = ["exportar_a_csv"]


@admin.register(Entidad)
class EntidadAdmin(AdminResource, admin.ModelAdmin):
    list_display = ('clave', 'nombreEntidad')
    ordering = ('clave', 'nombreEntidad')
    search_fields = ['clave', 'nombreEntidad']
    # list_filter = ('clave', 'nombreEntidad')
    list_per_page = 10
    empty_value_display = '-empty-'
    actions = ["exportar_a_csv"]


@admin.register(Municipio)
class MunicipioAdmin(AdminResource, admin.ModelAdmin):
    list_display = ('clave', 'nombreMunicipio')
    ordering = ('clave', 'nombreMunicipio')
    search_fields = ['clave', 'nombreMunicipio']
    # list_filter = ('clave', 'nombreMunicipio')
    list_per_page = 10
    empty_value_display = '-empty-'
    actions = ["exportar_a_csv"]


@admin.register(Asentamiento)
class AsentamientoAdmin(AdminResource, admin.ModelAdmin):
    list_display = ('clave', 'nombreAsentamiento', 'tipoZona', 'tipoAsentamiento')
    ordering = ('clave', 'nombreAsentamiento', 'tipoZona', 'tipoAsentamiento')
    search_fields = ['clave', 'nombreAsentamiento', 'tipoZona', 'tipoAsentamiento']
    # list_filter = ('clave', 'nombreAsentamiento', 'tipoZona', 'tipoAsentamiento')
    list_per_page = 10
    empty_value_display = '-empty-'
    actions = ["exportar_a_csv"]
