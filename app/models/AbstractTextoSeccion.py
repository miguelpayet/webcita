from django.db import models


class AbstractTextoSeccion(models.Model):
    idtexto = models.AutoField(primary_key=True)
    idioma = models.ForeignKey('Idioma', on_delete=models.CASCADE, db_column='ididioma')

    def __str__(self):
        return "%s %s" % (self.__class__, self.idtexto)

    def __unicode__(self):
        return u'%s %s' % (self.__class__, self.idtexto)

    class Meta:
        abstract = True
        managed = False

