def carrusel(opcion, cur_language, secciones):
    for i in opcion.seccioncarrusel_set.all():
        try:
            texto = i.textoseccioncarrusel_set.get(idioma__codigo=cur_language)
        except Exception:
            raise Exception("carrusel %s no tiene título" % i.nombre)
        clase = "col-md-" + str(int(round(12 / i.fotosfila)))
        list_fotos = obtener_fotos(i, cur_language)
        secciones.append({
            'carrusel': list_fotos, 'clase': clase, 'fotos': i.fotosfila, 'posicion': i.posicion, 'seccion': 'app/seccion_carrusel.html',
            'tipo': i.tipo, 'titulo': texto.titulo})


def obtener_fotos(seccion, cur_language):
    list_fotos = []
    qs_fotos = seccion.imagenseccioncarrusel_set.all().order_by('posicion')
    list_filas = []
    pos = 0
    for foto in qs_fotos:
        if len(list_fotos) == seccion.fotosfila:
            list_filas.append(list_fotos)
            list_fotos = []
        try:
            texto = foto.textoimagenseccioncarrusel_set.get(idioma__codigo=cur_language)
        except Exception:
            raise Exception("imagen tiene 0 o más de 1 texto en carrusel " + seccion.nombre)
        if seccion.tipo == 1:
            estilo = 'position:absolute; top:%s%%; left:%s%%; width:%s%%;color: #%s;' % (foto.posy, foto.posx, foto.ancho, foto.color)
        else:
            estilo = ''
        clase = (pos == 0 if "active" else "")
        list_fotos.append({'clase': clase, 'estilo': estilo, 'imagen': foto.imagen, 'pos': pos, 'texto': texto.texto})
        pos += 1
    list_filas.append(list_fotos)
    return list_filas
