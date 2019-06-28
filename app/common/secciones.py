from app.models import Contacto
from app.models import Idioma
from app.models import Parametro
from app.models import Social

from app.models.Contacto import TextoContacto


def contacto(cur_language):
    contact = Contacto.objects.first()
    if not contact:
        raise Exception("no hay registro de contacto")
    try:
        txt = contact.textocontacto_set.get(idioma__codigo=cur_language)
    except TextoContacto.DoesNotExist:
        raise Exception('no hay texto contacto para %s' % cur_language)
    list_social = []
    qs_social = Social.objects.all().order_by('posicion')
    for s in qs_social:
        list_social.append({'imagen': s.imagen, 'direccion': s.direccion, 'nombre': s.nombre})
    return {'direccion': contact.direccion, 'mapa': contact.mapa, 'mail': contact.mail, 'social': list_social,
            'telefonos': contact.telefonos, 'texto': txt, 'titulo': txt.titulo}


def idiomas(cur_language):
    idioma = Idioma.objects.get(codigo=cur_language)
    if not idioma:
        raise Exception("no existe idioma %s" % cur_language)
    arr_idioma = []
    for i in Idioma.objects.all().order_by('posicion'):
        arr_idioma.append({'nombre': i.nombre, 'codigo': i.codigo})
    return idioma, arr_idioma


# parametros
def parametros(cur_language):
    param = Parametro.objects.all().first()
    if not param:
        raise Exception("no hay registro de parámetros")
    try:
        txt = param.textoparametro_set.get(idioma__codigo=cur_language)
    except Exception:
        raise Exception('no hay texto parámetro para %s' % cur_language)
    return {'copyright': txt.copyright, 'logo_inferior': param.logomarron, 'logo_superior': param.logoblanco,
            'titulosocial': txt.titulosocial}


# sección texto
def texto(pagina, cur_language, secciones):
    for seccion in pagina.secciontexto_set.all():
        try:
            txt = seccion.textosecciontexto_set.get(idioma__codigo=cur_language)
        except Exception:
            raise Exception("texto tiene 0 o más de 1 texto %s", pagina.nombre)
        secciones.append({'nombre': seccion.nombre, 'posicion': seccion.posicion, 'seccion': 'app/seccion_texto.html',
                          'texto': txt.texto, 'tipo': seccion.tipo, 'titulo': txt.titulo})


# sección texto foto
def texto_foto(pagina, cur_language, secciones):
    for seccion in pagina.secciontextofoto_set.all():
        try:
            txt = seccion.textosecciontextofoto_set.get(idioma__codigo=cur_language)
        except Exception:
            raise Exception("texto foto tiene 0 o más de 1 texto %s", pagina.nombre)
        estilo = 'background-color: #%s;' % seccion.color
        secciones.append({'estilo': estilo, 'imagen': seccion.imagen, 'nombre': seccion.nombre, 'posicion': seccion.posicion,
                          'posicion_foto': seccion.posicion_foto, 'rango': range(2), 'seccion': 'app/seccion_texto_foto.html',
                          'subtipo': seccion.subtipo, 'texto': txt.texto, 'tipo': seccion.tipo, 'titulo': txt.titulo})
