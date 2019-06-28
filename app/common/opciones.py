from app.models import Opcion
from app.models import SubOpcion


def opciones(view_name, cur_language):
    # datos de las opciones
    arr_opcion = []
    for o in Opcion.objects.filter().order_by('posicion'):
        try:
            txt = o.textoopcion_set.get(idioma__codigo=cur_language)
        except Exception:
            raise Exception("opción tiene 0 o más de 1 texto en %s" % o.nombre)
        if o.subopcion_set.count() > 0:
            arr_subopcion = subopciones(o, cur_language)
            arr_opcion.append({'es_padre': True, 'handle': txt.direccion, 'titulo': txt.titulo, 'hijos': arr_subopcion})
        else:
            arr_opcion.append({'es_padre': False, 'handle': txt.direccion, 'titulo': txt.titulo})
    return arr_opcion


def opcion_actual(view_name):
    # opción actual
    try:
        opcion = Opcion.objects.get(nombre=view_name)
    except Opcion.DoesNotExist:
        try:
            opcion = SubOpcion.objects.get(nombre=view_name)
        except SubOpcion.DoesNotExist:
            raise Exception("vista %s no tiene opción o subopción" % view_name)
    return opcion


def subopciones(opcion, cur_language):
    arr_subopcion = []
    for so in opcion.subopcion_set.all().prefetch_related('pagina'):
        try:
            txt = so.textosubopcion_set.get(idioma__codigo=cur_language)
        except Exception:
            raise Exception("subopción tiene 0 o más de 1 texto en %s" % opcion.nombre)
        arr_subopcion.append({'handle': txt.direccion, 'titulo': txt.titulo})
    return arr_subopcion
