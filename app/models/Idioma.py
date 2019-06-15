from django.conf import settings
from django.db import models


class Idioma(models.Model):
    codigo = models.CharField(max_length=5)
    directorio = models.CharField(max_length=255, default=settings.MEDIA_ROOT, editable=False)
    ididioma = models.AutoField(primary_key=True)
    imagen = models.ImageField(max_length=255, blank=True)
    nombre = models.CharField(max_length=45)
    posicion = models.IntegerField()

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'idioma'
        managed = False
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
