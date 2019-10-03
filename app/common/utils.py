from operator import itemgetter

from django.http import Http404
from django.utils import translation

from opciones.common.Opciones import Opciones
from opciones.models.Pagina import Pagina
from opciones.models.Pagina import TextoPagina
from app.secciones.secciones import contacto
from app.secciones.secciones import idiomas
from app.secciones.secciones import parametros


def datos_comunes(view_name):
    # parametros
    cur_language = get_language()
    # idioma actual + lista de idiomas
    (idioma, arr_idioma) = idiomas(cur_language)
    # parametros
    params = parametros(idioma)
    # opciones y opción actual
    op = Opciones()
    arr_opcion = op.opciones(idioma, view_name)
    opcion = op.opcion_actual
    # la opcion actual puede tener none
    nombre_opcion = opcion.nombre if opcion else ''
    # datos de contacto
    contact = contacto(idioma)
    # pagina
    (pagina, dict_pagina) = get_pagina(opcion, view_name, idioma)
    # diccionario de contexto
    context = {'cur_language': idioma.codigo, 'contacto': contact, 'idiomas': arr_idioma, 'opcion_actual': nombre_opcion,
               'opciones': arr_opcion, 'pagina': dict_pagina, 'params': params}
    return context, idioma, pagina


def get_language():
    return translation.get_language()


def get_pagina(opcion, view_name, idioma):
    try:
        # opcion es None cuando la página no corresponde a una opción
        if opcion is None:
            # en este caso buscamos por view_name (nombre de la vista en duro o parámetro de url)
            pagina = Pagina.objects.prefetch_related('texto').get(nombre=view_name)
        else:
            pagina = Pagina.objects.prefetch_related('texto').get(opcion__nombre=opcion)
    except Pagina.DoesNotExist:
        if opcion is None:
            mensaje = 'página %s no existe' % view_name
        else:
            mensaje = 'opción %s no tiene página' % opcion
        raise Http404(mensaje)
    try:
        txt = pagina.texto.get(idioma=idioma)
    except TextoPagina.DoesNotExist:
        raise Exception("pagina %s no tiene texto en %s" % (pagina.nombre, idioma.nombre))
    return pagina, {'descripcion': txt.descripcion, 'titulo': txt.titulo}


# sortear las secciones por posicion
def sort_secciones(secciones):
    return sorted(secciones, key=itemgetter('posicion'))
