from django.db import models

from .AbstractTextoSeccion import AbstractTextoSeccion


class TextoSeccionTextoFoto(AbstractTextoSeccion):
    texto = models.TextField(max_length=1024)
    idseccion = models.ForeignKey('SeccionTextoFoto', on_delete=models.CASCADE, db_column='idseccion')

    class Meta:
        db_table = 'texto_seccion_texto_foto'
        managed = False
        verbose_name = 'Sección Texto con Foto'
        verbose_name_plural = 'Secciones Texto con Foto'
