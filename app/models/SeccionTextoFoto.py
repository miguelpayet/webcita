from django.db import models

from .AbstractSeccion import AbstractSeccion


class SeccionTextoFoto(AbstractSeccion):
    imagen = models.ImageField(max_length=50)
    tipo = models.IntegerField()
    color = models.CharField(max_length=6)

    class Meta:
        db_table = 'seccion_texto_foto'
        managed = False
        verbose_name = 'Sección Texto con Foto'
        verbose_name_plural = 'Secciones Texto con Foto'
