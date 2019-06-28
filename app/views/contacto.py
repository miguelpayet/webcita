from django.shortcuts import render

from app.common import carrusel
from app.common import utils


def contacto(request):
    # variables
    view_name = 'Contacto'
    (arr_idioma, arr_opcion, contact, cur_language, idioma, opcion, pagina, params) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, cur_language, secciones)
    # seccion contacto
    txt = contact['texto']
    dict_contacto = {'apellido': txt.apellido, 'comentarios': txt.comentarios, 'email': txt.email, 'nombre': txt.nombre,
                     'posicion': 2, 'seccion': 'app/seccion_contacto.html', 'mapa': contact['mapa'],  'titulo_email': txt.titulo_email}
    secciones.append(dict_contacto)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context = {'clase': 'contacto', 'contacto': contact, 'cur_language': cur_language, 'idiomas': arr_idioma, 'opciones': arr_opcion,
               'params': params, 'secciones': secciones}
    response = render(request, 'app/pagina.html', context)
    return response
