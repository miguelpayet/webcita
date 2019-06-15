from app.models import Contacto
from app.models import Idioma
from app.models import Opcion
from app.models import Parametro
from app.models import Social


# parte del pie
def contacto(cur_language):
    contact = Contacto.objects.all().first()
    if not contact:
        raise Exception("no hay registro de contacto")
    try:
        texto = contact.textocontacto_set.get(idioma__codigo=cur_language)
    except Exception:
        raise Exception('no hay texto contacto para %s' % cur_language)
    list_social = []
    qs_social = Social.objects.all().order_by('posicion')
    for s in qs_social:
        list_social.append({'imagen': s.imagen, 'direccion': s.direccion, 'nombre': s.nombre})
    return {'direccion': contact.direccion, 'mail': contact.mail, 'social': list_social, 'telefonos': contact.telefonos,
            'titulo': texto.titulo}


# parte del header
def idiomas(cur_language):
    idioma = Idioma.objects.get(codigo=cur_language)
    if not idioma:
        raise Exception("no existe idioma %s" % cur_language)
    arr_idioma = []
    for i in Idioma.objects.all().order_by('posicion'):
        arr_idioma.append({'nombre': i.nombre, 'codigo': i.codigo})
    return idioma, arr_idioma


# parte del header y del pie
def opciones(view_name, cur_language):
    opcion = None
    arr_opcion = []
    for o in Opcion.objects.filter().order_by('posicion'):
        try:
            texto = o.textoopcion_set.get(idioma__codigo=cur_language)
        except Exception:
            raise Exception("opción tiene 0 o más de 1 texto en %s" % o.nombre)
        arr_opcion.append({'handle': texto.direccion, 'titulo': texto.titulo})
        if o.nombre == view_name:
            opcion = o
    if not opcion:
        raise Exception('no existe opcion ' + view_name)
    return opcion, arr_opcion


# parametros
def parametros(cur_language):
    param = Parametro.objects.all().first()
    if not param:
        raise Exception("no hay registro de parámetros")
    try:
        texto = param.textoparametro_set.get(idioma__codigo=cur_language)
    except Exception:
        raise Exception('no hay texto parámetro para %s' % cur_language)
    return {'copyright': texto.copyright, 'logo_inferior': param.logomarron, 'logo_superior': param.logoblanco,
            'titulosocial': texto.titulosocial}


# sección texto foto
def texto_foto(opcion, cur_language, secciones):
    for seccion in opcion.secciontextofoto_set.all():
        try:
            texto = seccion.textosecciontextofoto_set.get(idioma__codigo=cur_language)
        except Exception:
            raise Exception("texto foto tiene 0 o más de 1 texto %s", opcion.nombre)
        estilo = 'background-color: #%s;' % seccion.color
        secciones.append({'estilo': estilo, 'imagen': seccion.imagen, 'nombre': seccion.nombre, 'posicion': seccion.posicion,
                          'rango': range(2), 'seccion': 'app/seccion_texto_foto.html', 'texto': texto.texto, 'tipo': seccion.tipo})
