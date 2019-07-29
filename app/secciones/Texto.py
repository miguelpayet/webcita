from app.models import SeccionTexto
from .SeccionBase import SeccionBase


class Texto(SeccionBase):
    template_seccion = 'secciones/texto-%s.html'

    def __call__(self, secciones):
        for seccion in self.vista.pagina.secciontexto_set.all():
            try:
                txt = seccion.textos.get(idioma=self.vista.idioma)
            except SeccionTexto.DoesNotExist:
                raise Exception("sección texto %s no tiene texto en %s", (self.vista.pagina.nombre, self.vista.idioma))
            secciones.append({'estilo': seccion.clase, 'nombre': seccion.nombre, 'posicion': seccion.posicion,
                              'seccion': self.template_seccion % seccion.tipo, 'texto': txt.texto, 'tipo': seccion.tipo,
                              'titulo': txt.titulo})
