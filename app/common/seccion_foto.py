from app.models import SeccionFoto


def foto(view_name, cur_language):
    # total y clase (en duro por ahora)
    total = 4
    clase = "col-md-" + str(int(round(12 / total)))
    sec_foto = SeccionFoto.objects.get(opcion__nombre=view_name)  # si solamente hay 1
    if not sec_foto:
        raise Exception('opción ' + view_name + ' no tiene seccion_foto en ' + cur_language)
    try:
        texto = sec_foto.textoseccionfoto_set.get(idioma__codigo=cur_language)
    except Exception:
        raise Exception("sección %s no tiene texto en %s" % (sec_foto.nombre, cur_language))
    arr_filas = []
    qs_filas = sec_foto.filaseccionfoto_set.all().order_by('posicion')
    for f in qs_filas:
        (offset, arr_fotos) = obtener_fotos(f, cur_language, total)
        arr_filas.append({'offset': offset, 'cantidad': len(arr_fotos), 'fotos': arr_fotos})
    return {'clase': clase, 'filas': arr_filas, 'nombre': sec_foto.nombre, 'posicion': sec_foto.posicion,
            'seccion': 'app/seccion_foto.html', 'titulo': texto.titulo}


def obtener_fotos(fila, cur_language, total):
    qs_fotos = fila.fotofilaseccionfoto_set.all().order_by('posicion')
    arr_fotos = [None] * total
    i = 0
    offset = total - qs_fotos.count()
    for f in qs_fotos:
        texto = next(iter(f.textofotofila_set.filter(idioma__codigo=cur_language)))
        if not texto:
            raise Exception('foto en fila ' + fila + " no tiene texto en " + cur_language)
        arr_fotos[i + offset] = {'imagen': f.imagen, 'texto': texto.texto}
        i += 1
    return offset, arr_fotos
