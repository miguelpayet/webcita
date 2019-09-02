from app.models import Idioma
from app.models import Social
from app.models import TextoParametro
from app.models.SeccionContacto import TextoContacto


def contacto(idioma):
    try:
        txt = TextoContacto.objects.select_related('contacto').get(idioma=idioma)
    except TextoContacto.DoesNotExist:
        raise Exception('no hay texto contacto para %s' % idioma.nombre)
    contact = txt.contacto
    list_social = social()
    return {'direccion': contact.direccion, 'estilo': contact.clase, 'mapa': contact.mapa, 'mail': contact.mail, 'social': list_social,
            'telefonos': contact.telefonos, 'texto': txt, 'titulo': txt.titulo}


def idiomas(cur_language):
    idioma = None
    arr_idioma = []
    for i in Idioma.objects.all().order_by('posicion'):
        if i.codigo == cur_language:
            idioma = i
        arr_idioma.append({'nombre': i.nombre, 'codigo': i.codigo})
    if not idioma:
        raise Exception("no existe idioma %s" % cur_language)
    return idioma, arr_idioma


# parametros
def parametros(idioma):
    try:
        txt = TextoParametro.objects.select_related('parametro').get(idioma=idioma)
    except TextoParametro.DoesNotExist:
        raise Exception('no hay registro de parámetros en %s' % idioma, idioma.codigo)
    return {'copyright': txt.copyright, 'logo_inferior': txt.parametro.logomarron, 'logo_superior': txt.parametro.logoblanco,
            'titulosocial': txt.titulosocial}


# data social
def social():
    list_social = []
    qs_social = Social.objects.all().order_by('posicion')
    for s in qs_social:
        list_social.append({'imagen': s.imagen, 'direccion': s.direccion, 'nombre': s.nombre})
    return list_social


# sección texto
def texto(pagina, idioma, secciones):
    for seccion in pagina.secciontexto_set.all():
        try:
            txt = seccion.textos.get(idioma=idioma)
        except Exception:
            raise Exception("texto tiene 0 o más de 1 texto %s", pagina.nombre)
        secciones.append({'nombre': seccion.nombre, 'posicion': seccion.posicion, 'seccion': 'texto.html',
                          'texto': txt.texto, 'tipo': seccion.tipo, 'titulo': txt.titulo})


# sección texto foto
def texto_foto(pagina, idioma, secciones):
    for seccion in pagina.secciontextofoto_set.all():
        try:
            txt = seccion.textos.get(idioma=idioma)
        except Exception:
            raise Exception("texto foto tiene 0 o más de 1 texto %s", pagina.nombre)
        estilo = 'background-color: #%s;' % seccion.color
        secciones.append({'estilo': estilo, 'imagen': seccion.imagen, 'nombre': seccion.nombre, 'posicion': seccion.posicion,
                          'posicion_foto': seccion.posicion_foto, 'rango': range(2), 'seccion': 'texto-foto-1.html',
                          'subtipo': seccion.subtipo, 'texto': txt.texto, 'tipo': seccion.tipo, 'titulo': txt.titulo})
