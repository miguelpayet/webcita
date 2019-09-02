from app.models import Opcion
from app.models import SubOpcion


def opciones(idioma, view_name):
    arr_opcion = []
    for o in Opcion.objects.order_by('posicion'):
        try:
            txt = o.textoopcion_set.get(idioma=idioma)
        except Exception:
            raise Exception("opción %s no tiene texto en %s" % (o.nombre, idioma))
        dict_opcion = {'handle': txt.direccion, 'titulo': txt.titulo}
        if o.subopcion_set.count() > 0:
            arr_subopcion = subopciones(o, idioma)
            activo = (len(list(filter(lambda x: x['nombre'] == view_name, arr_subopcion))) > 0)
            arr_opcion.append({**dict_opcion, 'active': 'active' if activo else '', 'es_padre': True, 'hijos': arr_subopcion})
        else:
            arr_opcion.append({**dict_opcion, 'active': 'active' if view_name == o.nombre else '', 'es_padre': False})
    return arr_opcion


def opcion_actual(view_name):
    try:
        opcion = Opcion.objects.get(nombre=view_name)
    except Opcion.DoesNotExist:
        try:
            opcion = SubOpcion.objects.get(nombre=view_name)
        except SubOpcion.DoesNotExist:
            # raise Exception("vista %s no tiene opción o subopción" % view_name)
            opcion = None
    return opcion


def subopciones(opcion, idioma):
    arr_subopcion = []
    for so in opcion.subopcion_set.all().prefetch_related('pagina'):
        try:
            txt = so.textosubopcion_set.get(idioma=idioma)
        except Exception:
            raise Exception("subopción %s no tiene texto en %s" % (opcion.nombre, idioma))
        arr_subopcion.append({'handle': txt.direccion, 'nombre': so.nombre, 'titulo': txt.titulo})
    return arr_subopcion
