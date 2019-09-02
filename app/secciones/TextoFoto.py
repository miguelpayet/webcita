from app.models import SeccionTextoFoto
from .SeccionBase import SeccionBase


class TextoFoto(SeccionBase):
    template_seccion = 'secciones/texto-foto-%s.html'

    def __call__(self, secciones):
        for seccion in self.vista.pagina.secciontextofoto_set.all():
            try:
                txt = seccion.textos.get(idioma=self.vista.idioma)
            except SeccionTextoFoto.DoesNotExist:
                raise Exception("texto foto tiene 0 o más de 1 texto %s", self.vista.pagina.nombre)
            estilo = 'background-color: #%s;' % seccion.color
            secciones.append(
                {'clase': seccion.clase, 'estilo': estilo, 'imagen': seccion.imagen, 'imagen_menor': seccion.imagen_menor,
                 'nombre': seccion.nombre, 'posicion': seccion.posicion, 'posicion_foto': seccion.posicion_foto, 'rango': range(2),
                 'seccion': self.template_seccion % seccion.tipo, 'subtipo': seccion.subtipo, 'texto': txt.texto, 'tipo': seccion.tipo,
                 'titulo': txt.titulo})
