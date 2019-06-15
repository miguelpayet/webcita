from django.db import models

from .AbstractTextoSeccion import AbstractTextoSeccion


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
        verbose_name = 'Texto Opción'
        verbose_name_plural = 'Textos Opción'
