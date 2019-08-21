from django.db import models

from .AbstractSeccion import AbstractSeccion
from .AbstractTextoSeccion import AbstractTextoSeccion


class SeccionFoto(AbstractSeccion):
    fotos = models.IntegerField(verbose_name='Fotos por fila')

    class Meta:
        db_table = 'seccion_foto'
        managed = False
        verbose_name = 'Sección Foto'
        verbose_name_plural = 'Secciones Foto'


class TextoSeccionFoto(AbstractTextoSeccion):
    titulo = models.CharField(max_length=45)
    seccion = models.ForeignKey('SeccionFoto', on_delete=models.CASCADE, db_column='idseccion')

    class Meta:
        db_table = 'texto_seccion_foto'
        managed = False
        verbose_name = 'Texto de Sección Foto'
        verbose_name_plural = 'Textos de Sección Foto'


class FilaSeccionFoto(models.Model):
    idfila = models.AutoField(primary_key=True)
    posicion = models.IntegerField()
    seccion = models.ForeignKey('SeccionFoto', on_delete=models.CASCADE, db_column='idseccion')

    def __str__(self):
        return "%s" % self.posicion

    def __unicode__(self):
        return u'%s' % self.posicion

    class Meta:
        db_table = 'fila_seccion_foto'
        managed = False
        verbose_name = 'Fila Sección Foto'
        verbose_name_plural = 'Filas Sección Foto'


class FotoFilaSeccionFoto(models.Model):
    clase = models.CharField(max_length=50, blank=True, verbose_name='Clase de diseño')
    idfoto = models.AutoField(primary_key=True)
    imagen = models.ImageField(max_length=50)
    posicion = models.IntegerField()
    seccion = models.ForeignKey('FilaSeccionFoto', on_delete=models.CASCADE, db_column='idfila', related_name='fotos')

    def __str__(self):
        return "%s" % self.posicion

    def __unicode__(self):
        return u'%s' % self.posicion

    class Meta:
        db_table = 'foto_fila'
        managed = False
        verbose_name = 'Foto de Fila Sección Foto'
        verbose_name_plural = 'Fotos de Fila Sección Foto'


class TextoFotoFila(AbstractTextoSeccion):
    texto = models.CharField(max_length=64)
    foto = models.ForeignKey('FotoFilaSeccionFoto', on_delete=models.CASCADE, db_column='idfoto')

    def __str__(self):
        return "%s" % self.texto

    def __unicode__(self):
        return u'%s' % self.texto

    class Meta:
        db_table = 'texto_foto_fila'
        managed = False
        verbose_name = 'Texto de Foto de Sección Foto'
        verbose_name_plural = 'Textos de Foto de Sección Foto'
