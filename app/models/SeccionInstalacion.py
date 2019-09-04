from django.db import models

from .AbstractSeccion import AbstractSeccion
from .AbstractTextoSeccion import AbstractTextoSeccion


class SeccionInstalacion(AbstractSeccion):
    total_fila = models.IntegerField(verbose_name='Fotos por fila')

    class Meta:
        db_table = 'instalacion'
        managed = False
        verbose_name = 'Instalación'
        verbose_name_plural = 'Secciones Instalación'


class TextoSeccionInstalacion(AbstractTextoSeccion):
    seccion = models.ForeignKey('SeccionInstalacion', on_delete=models.DO_NOTHING, db_column='idseccion')
    texto = models.TextField(max_length=512, blank=True)
    titulo = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        db_table = 'texto_instalacion'
        managed = False
        verbose_name = 'Texto de Instalación'
        verbose_name_plural = 'Textos de Instalación'


class FotoInstalacion(models.Model):
    idfoto = models.AutoField(primary_key=True)
    imagen = models.ImageField(max_length=50)
    seccion = models.ForeignKey('SeccionInstalacion', on_delete=models.DO_NOTHING, db_column='idseccion')

    def __str__(self):
        return "%s" % self.imagen

    def __unicode__(self):
        return u'%s' % self.imagen

    class Meta:
        db_table = 'foto_instalacion'
        managed = False
        verbose_name = 'Foto de Instalación'
        verbose_name_plural = 'Fotos de Instalación'


class TextoFotoInstalacion(AbstractTextoSeccion):
    foto = models.ForeignKey('FotoInstalacion', on_delete=models.DO_NOTHING, db_column='idfoto')
    titulo = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        db_table = 'texto_foto_instalacion'
        managed = False
        verbose_name = 'Texto de Foto'
        verbose_name_plural = 'Texto de Foto de Instalación'


class FotoFotoInstalacion(models.Model):
    foto = models.ForeignKey('FotoInstalacion', on_delete=models.DO_NOTHING, db_column='idfotopadre')
    idfoto = models.AutoField(primary_key=True)
    imagen = models.ImageField(max_length=50)

    def __str__(self):
        return "%s" % self.imagen

    def __unicode__(self):
        return u'%s' % self.imagen

    class Meta:
        db_table = 'foto_foto_instalacion'
        managed = False
        verbose_name = 'Foto de Foto Instalación'
        verbose_name_plural = 'Fotos de Foto Instalación'
