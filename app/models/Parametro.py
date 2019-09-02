from django.db import models

from .AbstractTextoSeccion import AbstractTextoSeccion


class Parametro(models.Model):
    idparametro = models.AutoField(primary_key=True)
    logoblanco = models.ImageField(max_length=50, verbose_name='Logo superior')
    logomarron = models.ImageField(max_length=50, verbose_name='Logo inferior')

    def __str__(self):
        return "%s %s" % ("Parámetro", self.idparametro)

    def __unicode__(self):
        return u'%s %s' % ("Parámetro", self.idparametro)

    class Meta:
        db_table = 'parametro'
        managed = False
        verbose_name = 'Parámetro'
        verbose_name_plural = 'Parámetros'


class TextoParametro(AbstractTextoSeccion):
    parametro = models.ForeignKey('Parametro', on_delete=models.DO_NOTHING, db_column='idparametro', related_name='textos')
    copyright = models.CharField(max_length=128)
    titulosocial = models.CharField(max_length=45)

    class Meta:
        db_table = 'texto_parametro'
        managed = False
        verbose_name = 'Valores'
        verbose_name_plural = 'Textos de Parámetro'
