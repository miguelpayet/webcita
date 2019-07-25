from django.db import models

from .AbstractSeccion import AbstractSeccion
from .AbstractTextoSeccion import AbstractTextoSeccion


class SeccionTextoFoto(AbstractSeccion):
    clase = models.CharField(max_length=20, blank=True, verbose_name='Clase')
    color = models.CharField(max_length=6)
    imagen = models.ImageField(max_length=50, blank=True)
    posicion_foto = models.IntegerField(verbose_name="Posicion izquierda o derecha", blank=True)
    subtipo = models.IntegerField(verbose_name="Estilo de margenes", blank=True)
    tipo = models.IntegerField(verbose_name="Estilo de título", blank=True)

    class Meta:
        db_table = 'seccion_texto_foto'
        managed = False
        verbose_name = 'Sección Texto con Foto'
        verbose_name_plural = 'Secciones Texto con Foto'


class TextoSeccionTextoFoto(AbstractTextoSeccion):
    texto = models.TextField(max_length=1024)
    titulo = models.CharField(max_length=128)
    idseccion = models.ForeignKey('SeccionTextoFoto', on_delete=models.CASCADE, db_column='idseccion', related_name='textos')

    class Meta:
        db_table = 'texto_seccion_texto_foto'
        managed = False
        verbose_name = 'Texto'
        verbose_name_plural = 'Textos'
