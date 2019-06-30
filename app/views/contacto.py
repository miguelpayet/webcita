from django.shortcuts import render

from app.common import carrusel
from app.common import utils


def contacto(request):
    # variables
    view_name = 'Contacto'
    (context, idioma, opcion, pagina) = utils.datos_comunes(view_name)
    # secciones
    secciones = []
    # carrusel
    carrusel(pagina, idioma, secciones)
    # seccion contacto
    contactin = context['contacto']
    txt = contactin['texto']
    dict_contacto = {'apellido': txt.apellido, 'comentarios': txt.comentarios, 'email': txt.email, 'nombre': txt.nombre,
                     'posicion': 2, 'seccion': 'app/seccion_contacto.html', 'mapa': contactin['mapa'],
                     'titulo_email': txt.titulo_email}
    secciones.append(dict_contacto)
    # sortear las secciones por posicion
    secciones = utils.sort_secciones(secciones)
    # invocar vista
    context.update(clase='contacto', secciones=secciones)
    response = render(request, 'app/pagina.html', context)
    return response
