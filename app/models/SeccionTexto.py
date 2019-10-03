from django.db import models

from opciones.models.AbstractSeccion import AbstractSeccion
from opciones.models.AbstractTextoSeccion import AbstractTextoSeccion


class SeccionTexto(AbstractSeccion):
    tipo = models.IntegerField()

    class Meta:
        db_table = 'seccion_texto'
        managed = False
        verbose_name = 'Sección Texto'
        verbose_name_plural = 'Secciones Texto'


class TextoSeccionTexto(AbstractTextoSeccion):
    titulo = models.CharField(max_length=128)
    texto = models.TextField(max_length=3072)
    idseccion = models.ForeignKey('SeccionTexto', on_delete=models.DO_NOTHING, db_column='idseccion', related_name='textos')

    class Meta:
        db_table = 'texto_seccion_texto'
        managed = False
        verbose_name = 'Texto'
        verbose_name_plural = 'Textos'
