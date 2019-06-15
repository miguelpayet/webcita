from django.db import models


class Opcion(models.Model):
    idopcion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    posicion = models.IntegerField()

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'opcion'
        managed = False
        verbose_name = 'Opción'
        verbose_name_plural = 'Opciones'
