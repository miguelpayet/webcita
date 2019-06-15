from django.db import models


class Social(models.Model):
    direccion = models.CharField(max_length=512)
    idsocial = models.AutoField(primary_key=True)
    imagen = models.ImageField(max_length=50)
    nombre = models.CharField(max_length=45)
    posicion = models.IntegerField()

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'social'
        managed = False
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
