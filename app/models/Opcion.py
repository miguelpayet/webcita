from django.db import models

from .AbstractTextoSeccion import AbstractTextoSeccion


class DatoOpcion(models.Model):
    iddato = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    pagina = models.ForeignKey('Pagina', on_delete=models.DO_NOTHING, db_column='idpagina')
    posicion = models.IntegerField()

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'dato_opcion'
        managed = False
        verbose_name = 'Opción'
        verbose_name_plural = 'Opciones'


class TextoDatoOpcion(AbstractTextoSeccion):
    direccion = models.CharField(max_length=255, blank=True)
    dato = models.ForeignKey('DatoOpcion', on_delete=models.DO_NOTHING, db_column='iddato')
    titulo = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % self.titulo

    def __unicode__(self):
        return u'%s' % self.titulo

    class Meta:
        db_table = 'texto_dato'
        managed = False
        verbose_name = 'Texto de opción'
        verbose_name_plural = 'Textos de opción'


class Opcion(models.Model):
    idopcion = models.AutoField(primary_key=True)
    dato = models.OneToOneField(DatoOpcion, on_delete=models.DO_NOTHING, db_column='iddato')

    def __str__(self):
        return "%s" % self.idopcion

    def __unicode__(self):
        return u'%s' % self.idopcion

    class Meta:
        db_table = 'dato_opcion'
        managed = False
        verbose_name = 'Dato de opción'
        verbose_name_plural = 'Datos de opción'


class SubOpcion(models.Model):
    idsubopcion = models.AutoField(primary_key=True)
    dato = models.OneToOneField(DatoOpcion, on_delete=models.DO_NOTHING, db_column='iddato')

    def __str__(self):
        return "%s" % self.idsubopcion

    def __unicode__(self):
        return u'%s' % self.idsubopcion

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
