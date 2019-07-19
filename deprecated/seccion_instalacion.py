from app.models import FotoFotoInstalacion
from app.models import SeccionInstalacion
from app.models import TextoFotoInstalacion
from app.models import TextoSeccionInstalacion


def instalacion(view_name, idioma, secciones):
    try:
        seccion = SeccionInstalacion.objects.get(nombre=view_name)
        try:
            txt = seccion.textoseccioninstalacion_set.get(idioma=idioma)
        except TextoSeccionInstalacion.DoesNotExist as ex:
            raise Exception("no existe texto para instalación %s" % view_name)
        arr_filas = fotos_instalacion(seccion, idioma)
        clase = "col-md-%s" % (12 // seccion.total_fila)
        dict_seccion = {'clase': clase, 'filas': arr_filas, 'posicion': seccion.posicion, 'seccion': 'seccion_instalacion.html',
                        'titulo': txt.titulo}
        secciones.append(dict_seccion)
    except SeccionInstalacion.DoesNotExist:
        raise Exception("no existe sección instalación para %s" % view_name)


def fotos_instalacion(seccion, idioma):
    active = True
    pos = 0
    total = seccion.total_fila
    arr_filas = []
    arr_fotos = [None] * total
    for foto in seccion.fotoinstalacion_set.all():
        txt = None
        try:
            txt = foto.textofotoinstalacion_set.get(idioma=idioma)
        except TextoFotoInstalacion.DoesNotExist:
            raise Exception("no existe texto para foto %s en instalación %s" % (foto.imagen, seccion.nombre))
        arr_detalle = fotos_instalacion_detalle(foto.idfoto)
        dict_hijo = {'active': active, 'fotos': arr_detalle, 'texto': txt.texto}
        arr_fotos[pos] = {'active': active, 'id': foto.idfoto, 'imagen': foto.imagen, 'texto': txt.titulo, 'hijo': dict_hijo}
        active = False
        if (pos + 1) == total:
            arr_filas.append({'active': tiene_foto_activa(arr_fotos), 'fotos': arr_fotos})
        pos += 1
    if pos < total:  # añadir última fila
        arr_filas.append(arr_filas)
    return arr_filas


def fotos_instalacion_detalle(idfoto):
    qs_fotos = FotoFotoInstalacion.objects.filter(foto__idfoto=idfoto)
    if qs_fotos.count() == 0:
        raise Exception('no existen fotos para foto de instalación con id %s' % idfoto)
    arr_fotos = list(map(lambda x: {'imagen': x.imagen}, qs_fotos.all()))
    return arr_fotos


def tiene_foto_activa(arr_fotos):
    lista = list(filter(lambda x: x['active'], arr_fotos))
    return True if len(lista) > 0 else False
