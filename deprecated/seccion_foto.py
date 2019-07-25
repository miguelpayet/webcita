from app.models import SeccionFoto
from app.models import TextoFotoFila
from app.models import TextoSeccionFoto


def foto(view_name, idioma, secciones):
    sec_foto = SeccionFoto.objects.get(pagina__opcion__nombre=view_name)  # si solamente hay 1
    if not sec_foto:
        raise Exception('opción %s no tiene seccion_foto en %s' % (view_name, idioma.codigo))
    # total y clase
    total = sec_foto.fotos
    clase = "col-md-" + str(int(round(12 / total)))
    try:
        txt = sec_foto.textoseccionfoto_set.get(idioma=idioma)
    except TextoSeccionFoto.DoesNotExist:
        txt = None
    arr_filas = []
    qs_filas = sec_foto.filaseccionfoto_set.all().order_by('posicion')
    for f in qs_filas:
        (offset, arr_fotos) = obtener_fotos(f, idioma, total)
        arr_filas.append({'offset': offset, 'cantidad': len(arr_fotos), 'fotos': arr_fotos})
    dict_foto = {'clase': clase, 'filas': arr_filas, 'nombre': sec_foto.nombre, 'posicion': sec_foto.posicion,
                 'seccion': 'foto.html', 'titulo': txt.titulo if txt else ''}
    secciones.append(dict_foto)


def obtener_fotos(fila, idioma, total):
    qs_fotos = fila.fotofilaseccionfoto_set.all().order_by('posicion')
    arr_fotos = [None] * total
    i = 0
    offset = total - qs_fotos.count()
    txt = None
    for f in qs_fotos:
        try:
            txt = f.textofotofila_set.get(idioma=idioma)
        except TextoFotoFila.DoesNotExist:
            txt = None
        arr_fotos[i + offset] = {'clase': f.clase, 'imagen': f.imagen, 'texto': txt.texto if txt else ''}
        i += 1
    return offset, arr_fotos
