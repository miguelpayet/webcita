from app.models import SeccionInstalacion
from app.models import TextoFotoInstalacion
from app.models import TextoSeccionInstalacion
from .SeccionBase import SeccionBase


class Instalacion(SeccionBase):
    template_seccion = 'secciones/instalacion.html'

    def __call__(self, secciones):
        for seccion in SeccionInstalacion.objects.filter(pagina__nombre=self.vista.pagina).all():
            try:
                txt = seccion.textoseccioninstalacion_set.get(idioma=self.vista.idioma)
            except TextoSeccionInstalacion.DoesNotExist:
                raise Exception("no existe texto para instalación %s" % self.vista.view_name)
            arr_fotos = self.fotos_instalacion(seccion)
            dict_seccion = {'clase': seccion.clase, 'fotos': arr_fotos, 'posicion': seccion.posicion, 'seccion': self.template_seccion,
                            'texto': txt.texto, 'titulo': txt.titulo}
            secciones.append(dict_seccion)

    def fotos_instalacion(self, seccion):
        pos = 0
        total = seccion.total_fila
        arr_fotos = []
        for foto in seccion.fotoinstalacion_set.all():
            try:
                txt = foto.textofotoinstalacion_set.get(idioma=self.vista.idioma)
                titulo = txt.titulo
            except TextoFotoInstalacion.DoesNotExist:
                titulo = None
                # raise Exception("no existe texto para foto %s en instalación %s" % (foto.imagen, seccion.nombre))
            arr_fotos.append({'imagen': foto.imagen, 'titulo': txt.titulo})
        return arr_fotos
