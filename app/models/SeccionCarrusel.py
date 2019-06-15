from django.db import models

from .AbstractSeccion import AbstractSeccion
from .AbstractTextoSeccion import AbstractTextoSeccion


class SeccionCarrusel(AbstractSeccion):
    fotosfila = models.IntegerField(verbose_name='Fotos por fila')
    tipo = models.IntegerField()

    class Meta:
        db_table = 'seccion_carrusel'
        managed = False
        verbose_name = 'Carrusel'
        verbose_name_plural = 'Carruseles'


class ImagenSeccionCarrusel(models.Model):
    ancho = models.IntegerField()
    color = models.CharField(max_length=6)
    idimagen = models.AutoField(primary_key=True)
    imagen = models.ImageField(max_length=50)
    posicion = models.IntegerField()
    posx = models.IntegerField()
    posy = models.IntegerField()
    seccion = models.ForeignKey('SeccionCarrusel', on_delete=models.CASCADE, db_column='idseccion')

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
    imagen = models.ForeignKey('ImagenSeccionCarrusel', on_delete=models.CASCADE, db_column='idimagen')
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
    seccion = models.ForeignKey('SeccionCarrusel', on_delete=models.CASCADE, db_column='idseccion')

    class Meta:
        db_table = 'texto_seccion_carrusel'
        managed = False
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos Carrusel'
