from django.db import models

from opciones.models.AbstractTextoSeccion import AbstractTextoSeccion


class Pagina(models.Model):
    idpagina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'pagina'
        managed = False
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'


class TextoPagina(AbstractTextoSeccion):
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=512)
    pagina = models.ForeignKey('Pagina', on_delete=models.DO_NOTHING, db_column='idpagina', related_name='texto')

    class Meta:
        db_table = 'texto_pagina'
        managed = False
        verbose_name = 'Texto Página'
        verbose_name_plural = 'Textos Página'
