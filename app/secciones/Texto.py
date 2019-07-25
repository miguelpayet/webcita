from .SeccionBase import SeccionBase


class Texto(SeccionBase):
    template_seccion = 'secciones/texto-%s.html'

    def __call__(self, secciones):
        for seccion in self.vista.pagina.secciontexto_set.all():
            try:
                txt = seccion.textos.get(idioma=self.vista.idioma)
            except Exception:
                raise Exception("texto tiene 0 o más de 1 texto %s", self.vista.pagina.nombre)
            secciones.append({'nombre': seccion.nombre, 'posicion': seccion.posicion, 'seccion': self.template_seccion % seccion.tipo,
                              'texto': txt.texto, 'tipo': seccion.tipo, 'titulo': txt.titulo})
