from django.db import models


class AbstractSeccion(models.Model):
    idseccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    pagina = models.ForeignKey('Pagina', on_delete=models.CASCADE, db_column='idpagina')
    posicion = models.IntegerField()

    class Meta:
        abstract = True
        managed = False

    def __str__(self):
        return "%s" % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre
