from django.core.exceptions import MultipleObjectsReturned

from app.models.SeccionCarrusel import TextoImagenSeccionCarrusel
from app.models.SeccionCarrusel import TextoSeccionCarrusel


def carrusel(pagina, idioma, secciones):
    for i in pagina.seccioncarrusel_set.all():
        titulo = ""
        if i.tipo == 2:
            try:
                texto = i.textoseccioncarrusel_set.get(idioma=idioma)
                titulo = texto.titulo
            except (MultipleObjectsReturned, TextoSeccionCarrusel.DoesNotExist):
                raise Exception("carrusel %s no tiene título" % i.nombre)
        if i.tipo == 3:
            clase = "col-md-10 offset-md-1"
        else:
            clase = "col-md-" + str(int(round(12 / i.fotosfila)))
        list_fotos = obtener_fotos(i, idioma)
        secciones.append({
            'carrusel': list_fotos, 'clase': clase, 'fotos': i.fotosfila, 'posicion': i.posicion, 'seccion': 'app/seccion_carrusel.html',
            'tipo': i.tipo, 'titulo': titulo})


def obtener_fotos(seccion, idioma):
    list_fotos = []
    qs_fotos = seccion.imagenseccioncarrusel_set.all().order_by('posicion')
    list_filas = []
    pos = 0
    for foto in qs_fotos:
        if len(list_fotos) == seccion.fotosfila:
            list_filas.append(list_fotos)
            list_fotos = []
        try:
            texto = foto.textoimagenseccioncarrusel_set.get(idioma=idioma)
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