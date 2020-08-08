from django.db import models

from opciones.models.AbstractSeccion import AbstractSeccion
from opciones.models.AbstractTextoSeccion import AbstractTextoSeccion


class SeccionTextoFoto(AbstractSeccion):
    color = models.CharField(max_length=6)
    imagen = models.ImageField(max_length=50, verbose_name='Imagen principal')
    imagen_menor = models.ImageField(max_length=50, blank=True, verbose_name='Imagen secundaria (opcional)')
    posicion_foto = models.IntegerField(verbose_name="Posicion izquierda o derecha (opcional)", blank=True)
    subtipo = models.IntegerField(verbose_name="Estilo de margenes (opcional)", blank=True)
    tipo = models.IntegerField(verbose_name="Tipo de sección")

    class Meta:
        db_table = 'seccion_texto_foto'
        managed = False
        verbose_name = 'Sección Texto con Foto'
        verbose_name_plural = 'Secciones Texto con Foto'


class TextoSeccionTextoFoto(AbstractTextoSeccion):
    texto = models.TextField(max_length=1024)
    titulo = models.CharField(max_length=128, blank=True, verbose_name='Título (opcional)')
    idseccion = models.ForeignKey('SeccionTextoFoto', on_delete=models.DO_NOTHING, db_column='idseccion', related_name='textos')

    class Meta:
        db_table = 'texto_seccion_texto_foto'
        managed = False
        verbose_name = 'Texto'
        verbose_name_plural = 'Textos'
