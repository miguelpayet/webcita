from django.db import models

from opciones.models.AbstractSeccion import AbstractSeccion
from opciones.models.AbstractTextoSeccion import AbstractTextoSeccion


class SeccionCarrusel(AbstractSeccion):
    fotosfila = models.IntegerField(verbose_name='Fotos por fila')
    tipo = models.IntegerField()

    class Meta:
        db_table = 'seccion_carrusel'
        managed = False
        verbose_name = 'Carrusel'
        verbose_name_plural = 'Carruseles'


class ImagenSeccionCarrusel(models.Model):
    ancho = models.IntegerField(blank=True)
    color = models.CharField(max_length=6, blank=True)
    destino = models.CharField(max_length=200, blank=True, verbose_name='Dirección destino (opcional)')
    idimagen = models.AutoField(primary_key=True)
    imagen = models.ImageField(max_length=50)
    posicion = models.IntegerField()
    posx = models.IntegerField(blank=True)
    posy = models.IntegerField(blank=True)
    seccion = models.ForeignKey('SeccionCarrusel', on_delete=models.DO_NOTHING, db_column='idseccion')

    def __str__(self):
        return "%s" % self.idimagen

    def __unicode__(self):
        return u'%s' % self.idimagen

    class Meta:
        db_table = 'imagen_seccion_carrusel'
        managed = False
        verbose_name = 'Imágen'
        verbose_name_plural = 'Imágenes Sección Carrusel'


class TextoImagenSeccionCarrusel(AbstractTextoSeccion):
    imagen = models.ForeignKey('ImagenSeccionCarrusel', on_delete=models.DO_NOTHING, db_column='idimagen')
    texto = models.CharField(max_length=255)

    def __str__(self):
        return '% s( %s)' % (self.imagen, self.texto)

    def __unicode__(self):
        return u'%s (%s)' % (self.imagen, self.texto)

    class Meta:
        db_table = 'texto_imagen'
        managed = False
        verbose_name = 'Texto de la Imagen'
        verbose_name_plural = 'Textos de Imagen de Sección Carrusel'


class TextoSeccionCarrusel(AbstractTextoSeccion):
    titulo = models.CharField(max_length=45)
    seccion = models.ForeignKey('SeccionCarrusel', on_delete=models.DO_NOTHING, db_column='idseccion')

    class Meta:
        db_table = 'texto_seccion_carrusel'
        managed = False
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos Carrusel'
