from django.db import models


class Pagina(models.Model):
    idpagina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return '%s' % self.nombre

    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        db_table = 'pagina'
        managed = False
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'
