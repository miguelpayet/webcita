from app.models import SeccionFoto
from app.models import TextoFotoFila
from app.models import TextoSeccionFoto
from .SeccionBase import SeccionBase


class Foto(SeccionBase):
    template_seccion = 'secciones/foto.html'

    def __call__(self, secciones):
        try:
            sec_foto = SeccionFoto.objects.get(pagina__opcion__nombre=self.vista.view_name)
        except SeccionFoto.DoesNotExist:
            raise Exception('opción %s no tiene seccion_foto' % self.vista.view_name)
        # total de fotos
        total_fotos = sec_foto.fotos
        # columnas por foto
        columnas_foto = int(round(12 / total_fotos))
        clase = "col-md-%s" % str(columnas_foto)
        try:
            txt = sec_foto.textoseccionfoto_set.get(idioma=self.vista.idioma)
        except TextoSeccionFoto.DoesNotExist:
            txt = None
        arr_filas = []
        qs_filas = sec_foto.filaseccionfoto_set.all().order_by('posicion')
        for f in qs_filas:
            arr_fotos = self.obtener_fotos(f, total_fotos)
            # cantidad de columnas antes de la primera foto
            offset = (total_fotos - len(arr_fotos))
            clase_offset = 'offset-md-%s' % str(offset * columnas_foto) if offset > 0 else ''
            arr_filas.append({'cantidad': len(arr_fotos), 'fotos': arr_fotos, 'offset': clase_offset})
        dict_foto = {'clase': clase, 'estilo': sec_foto.clase, 'filas': arr_filas, 'nombre': sec_foto.nombre,
                     'posicion': sec_foto.posicion, 'seccion': self.template_seccion, 'titulo': txt.titulo if txt else ''}
        secciones.append(dict_foto)

    def obtener_fotos(self, fila, total_fotos):
        qs_fotos = fila.fotos.all().order_by('posicion')
        arr_fotos = []
        for f in qs_fotos:
            try:
                txt = f.textofotofila_set.get(idioma=self.vista.idioma)
            except TextoFotoFila.DoesNotExist:
                txt = None
            arr_fotos.append({'clase': f.clase, 'imagen': f.imagen, 'texto': txt.texto if txt else ''})
        return arr_fotos
