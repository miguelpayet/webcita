from django.core.exceptions import MultipleObjectsReturned

from app.models.SeccionCarrusel import TextoImagenSeccionCarrusel
from app.models.SeccionCarrusel import TextoSeccionCarrusel
from .SeccionBase import SeccionBase


class Carrusel(SeccionBase):
    template_seccion = 'secciones/carrusel-%s.html'

    def __call__(self, secciones):
        for seccion in self.vista.pagina.seccioncarrusel_set.all():
            titulo = ""
            if seccion.tipo == 2:
                try:
                    texto = seccion.textoseccioncarrusel_set.get(idioma=self.vista.idioma)
                    titulo = texto.titulo
                except (MultipleObjectsReturned, TextoSeccionCarrusel.DoesNotExist):
                    raise Exception("carrusel %s no tiene título" % seccion.nombre)
            if seccion.tipo == 3:
                columnas = "col-md-10 offset-md-1"
            elif seccion.tipo == 2:
                columnas = "col-md-" + str(int(round(10 / seccion.fotosfila)))
            else:
                columnas = "col-md-" + str(int(round(12 / seccion.fotosfila)))
            secciones.append(
                {'carrusel': self.obtener_fotos(seccion), 'clase': seccion.clase, 'columnas': columnas, 'fotos': seccion.fotosfila,
                 'posicion': seccion.posicion, 'seccion': self.template_seccion % seccion.tipo, 'tipo': seccion.tipo, 'titulo': titulo})

    def obtener_fotos(self, seccion):
        list_fotos = []
        qs_fotos = seccion.imagenseccioncarrusel_set.all().order_by('posicion')
        list_filas = []
        pos = 0
        for foto in qs_fotos:
            if len(list_fotos) == seccion.fotosfila:
                list_filas.append(list_fotos)
                list_fotos = []
            try:
                texto = foto.textoimagenseccioncarrusel_set.get(idioma=self.vista.idioma)
                texto_foto = texto.texto
            except (MultipleObjectsReturned, TextoImagenSeccionCarrusel.DoesNotExist):
                if seccion.tipo != 3:
                    raise Exception("imagen tiene 0 o más de 1 texto en carrusel " + seccion.nombre)
                else:
                    texto_foto = ''
            if seccion.tipo == 1:
                estilo = 'position:absolute; top:%s%%; left:%s%%; width:%s%%;color: #%s;' % (foto.posy, foto.posx, foto.ancho, foto.color)
            else:
                estilo = ''
            clase = (pos == 0 if "active" else "")
            list_fotos.append({'clase': clase, 'estilo': estilo, 'imagen': foto.imagen, 'pos': pos, 'texto': texto_foto})
            pos += 1
        list_filas.append(list_fotos)
        return list_filas
