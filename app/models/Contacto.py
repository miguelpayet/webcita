from django.db import models


class Contacto(models.Model):
    idcontacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    comments = models.TextField(max_length=2048)

    def __str__(self):
        return "%s" % self.idcontacto

    def __unicode__(self):
        return u'%s' % self.idcontacto

    class Meta:
        db_table = 'contacto'
        managed = False
        verbose_name = 'Contacto Recibido'
        verbose_name_plural = 'Contactos Recibidos'
