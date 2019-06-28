from django.db import models

from .AbstractTextoSeccion import AbstractTextoSeccion


class Contacto(models.Model):
    direccion = models.TextField(max_length=512)
    idcontacto = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=45)
    mapa = models.ImageField(max_length=50)
    telefonos = models.TextField(max_length=512)

    def __str__(self):
        return "%s" % self.idcontacto

    def __unicode__(self):
        return u'%s' % self.idcontacto

    class Meta:
        db_table = 'contacto'
        managed = False
        verbose_name = 'Dato de Contacto'
        verbose_name_plural = 'Datos de Contacto'


class TextoContacto(AbstractTextoSeccion):
    apellido = models.CharField(max_length=45)
    comentarios = models.CharField(max_length=45)
    contacto = models.ForeignKey('Contacto', on_delete=models.CASCADE, db_column='idcontacto')
    email = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    titulo = models.CharField(max_length=45)
    titulo_email = models.CharField(max_length=45)

    class Meta:
        db_table = 'texto_contacto'
        managed = False
        verbose_name = 'Texto de Contacto'
        verbose_name_plural = 'Textos de Contacto'
