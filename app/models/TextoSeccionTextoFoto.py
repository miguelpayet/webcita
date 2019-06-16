from django.db import models

from .AbstractTextoSeccion import AbstractTextoSeccion


class TextoSeccionTextoFoto(AbstractTextoSeccion):
    texto = models.TextField(max_length=1024)
    titulo = models.CharField(max_length=128)
    idseccion = models.ForeignKey('SeccionTextoFoto', on_delete=models.CASCADE, db_column='idseccion')

    class Meta:
        db_table = 'texto_seccion_texto_foto'
        managed = False
        verbose_name = 'Texto'
        verbose_name_plural = 'Textos'
