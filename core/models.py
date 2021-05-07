from unicodedata import decimal

from django.db import models


# Create your models here.
class Informacion(models.Model):
    privacidad = models.TextField(verbose_name='Política de privacidad', max_length=5000)
    nombre = models.CharField(verbose_name='Nombre de la aplicación', max_length=100)
    nombreContro = models.CharField(verbose_name='Nombre corto', max_length=20)
    telefono = models.CharField(verbose_name='Contacto', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombreContro

    class Meta:
        verbose_name = 'Información'
        verbose_name_plural = 'Datos de la aplicación'


# Temperaturas
class Temperatura(models.Model):
    temperaturaMinima = models.DecimalField(verbose_name='Temperatura mínima', max_digits=2, decimal_places=2,
                                            default=0.00)
    temperaturaMaxima = models.DecimalField(verbose_name='Temperatura máxima', max_digits=2, decimal_places=2,
                                            default=0.00)
    temperaturaLeida = models.DecimalField(verbose_name='Temperatura leída', max_digits=2, decimal_places=2,
                                           default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.temperaturaLeida

    class Meta:
        verbose_name = 'Temperatuta'
        verbose_name_plural = 'Temperaturas'


class Entidad(models.Model):
    clave = models.CharField(verbose_name='Clave', max_length=10)
    nombreEntidad = models.CharField(verbose_name='Entidad', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombreEntidad

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Municipio(models.Model):
    Entidad = models.ForeignKey(Entidad, verbose_name='Entidad', on_delete=models.CASCADE)
    clave = models.CharField(verbose_name='Clave', max_length=10)
    nombreMunicipio = models.CharField(verbose_name='Municipio', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombreMunicipio

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'


class Asentamiento(models.Model):
    Municipio = models.ForeignKey(Municipio, verbose_name='Municipio', on_delete=models.CASCADE)
    clave = models.CharField(verbose_name='Clave', max_length=10)
    nombreAsentamiento = models.CharField(verbose_name='Asentamiento', max_length=50)
    ZONA = {('Rural', 'Rural'), ('Semi urbana', 'Semi urbana'), ('Urbana', 'Urbana')}
    tipoZona = models.CharField(verbose_name='Tipo de zona', choices=ZONA, default='Rural', max_length=11)
    ASE = {('Pueblo', 'Pueblo'), ('Ejido', 'Ejido'), ('Ranchería', 'Ranchería')}
    tipoAsentamiento = models.CharField(verbose_name='Tipo', choices=ASE, default='Ejido', max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombreAsentamiento

    class Meta:
        verbose_name = 'Asentamiento'
        verbose_name_plural = 'Asentamientos'


class Area(models.Model):
    clave = models.CharField(verbose_name='Clave', max_length=10)
    nombre = models.CharField(verbose_name='Lugar', max_length=200)
    Asentamiento = models.ForeignKey(Asentamiento, verbose_name='Asentamiento', on_delete=models.DO_NOTHING)
    altitud = models.CharField(verbose_name='Altitud', max_length=20, null=True)
    latitud = models.CharField(verbose_name='Latitud', max_length=12, null=True)
    longitud = models.CharField(verbose_name='Longitud', max_length=12, null=True)
    OP = {('Sí', 'Sí'), ('No', 'No')}
    operando = models.CharField(verbose_name='Activo', default='No', choices=OP, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Datos de la ubicación'


class PlanDeContingencia(models.Model):
    area = models.ForeignKey(Area, verbose_name='área', on_delete=models.DO_NOTHING)
    nombre = models.CharField(verbose_name='Nombre del plan', max_length=255)
    OPCIONES = {('Desconocido', 'Desconocido'), ('Iniciado', 'Iniciado'), ('En proceso', 'En proceso'),
                ('Finalizado', 'Finalizado'), ('En Evaluación', 'En Evaluación')}
    activo = models.CharField(verbose_name='Estado del plan', choices=OPCIONES, max_length=13, default='Desconocido')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Plan de contingencia'
        verbose_name_plural = 'Planes de contingencia'


class MonitorSequia(models.Model):
    intensidad = models.CharField(verbose_name='Intensidad de la sequía', max_length=50)
    descripcion = models.TextField(verbose_name='Descripción', max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.intensidad

    class Meta:
        verbose_name = 'Monitor de sequía'
        verbose_name_plural = 'Datos de la sequía'


class Analisis(models.Model):
    titulo = models.CharField(verbose_name='Nombre del análisis', max_length=255)
    periodo = models.CharField(verbose_name='Periodo', max_length=100)
    fechaInicio = models.DateField(verbose_name='Fecha de inicio')
    fechaFin = models.DateField(verbose_name='Fecha de fin')
    fechaPaso = models.DateField(verbose_name='Fecha de paso')
    archivo = models.FileField(verbose_name='Archivo')
    tipoAnalisis = models.CharField(verbose_name='Tipo de análisis', max_length=100)
    comentario = models.CharField(verbose_name='Comentario', null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Análisis'
        verbose_name_plural = 'Análisis'


class Cultivos(models.Model):
    nombre = models.CharField(verbose_name='Cultivo', max_length=150)
    nombreCientifico = models.CharField(verbose_name='Nombre científico', max_length=100)
    descripcion = models.TextField(verbose_name='Descripcion', max_length=5000)
    imagenes = models.ImageField(verbose_name='Foto', upload_to='imgcultivos')
    MESES = {
        ('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'),
        ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')
    }
    mesDeSiembra = models.CharField(verbose_name='Mes de siembra', choices=MESES, max_length=30, default='Enero')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'


class CensoTemperatura(models.Model):
    Area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, verbose_name='Area')
    Cultivo = models.ForeignKey(Cultivos, on_delete=models.DO_NOTHING, verbose_name='Cultivo')
    temperatura1 = models.DecimalField(verbose_name='Temperatura del suelo', max_digits=5, decimal_places=1,
                                       default=26.0, max_length=6)
    temperatura2 = models.DecimalField(verbose_name='Temperatura ambiental', max_digits=5, decimal_places=1,
                                       default=27.0,
                                       max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.temperatura1)

    class Meta:
        verbose_name = 'Temperatura'
        verbose_name_plural = 'Temperatura'
