from django.db import models

from .AbstractTextoSeccion import AbstractTextoSeccion


class Opcion(models.Model):
    idopcion = models.AutoField(primary_key=True)
    idpadre = models.IntegerField(verbose_name='Identificador de la opción principal')
    nombre = models.CharField(max_length=45)
    pagina = models.ForeignKey('Pagina', on_delete=models.DO_NOTHING, db_column='idpagina', )
    posicion = models.IntegerField()
    tipo = models.IntegerField()

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
    direccion = models.CharField(max_length=255, blank=True)
    opcion = models.ForeignKey('Opcion', on_delete=models.DO_NOTHING, db_column='idopcion', related_name='texto')
    titulo = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        db_table = 'texto_opcion'
        managed = False
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalle'


class SubOpcion(models.Model):
    idsubopcion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    opcion = models.ForeignKey('Opcion', on_delete=models.DO_NOTHING, db_column='idopcion')
    pagina = models.ForeignKey('Pagina', on_delete=models.DO_NOTHING, db_column='idpagina')
    posicion = models.IntegerField()

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'subopcion'
        managed = False
        verbose_name = 'Sub Opción'
        verbose_name_plural = 'Sub Opciones'


class TextoSubOpcion(AbstractTextoSeccion):
    direccion = models.CharField(max_length=255, blank=True)
    subopcion = models.ForeignKey('SubOpcion', on_delete=models.DO_NOTHING, db_column='idsubopcion')
    titulo = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        db_table = 'texto_subopcion'
        managed = False
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalle'
