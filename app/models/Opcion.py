from django.db import models

from .AbstractTextoSeccion import AbstractTextoSeccion


class Opcion(models.Model):
    idopcion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    posicion = models.IntegerField()

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'opcion'
        managed = False
        verbose_name = 'Opción'
        verbose_name_plural = 'Opciones'


class TextoOpcion(AbstractTextoSeccion):
    opcion = models.ForeignKey('Opcion', on_delete=models.CASCADE, db_column='idopcion')
    titulo = models.CharField(max_length=45)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        db_table = 'texto_opcion'
        managed = False
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalle'
