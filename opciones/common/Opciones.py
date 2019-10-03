from opciones.models import TextoOpcion


class Opciones:

    def __init__(self):
        self.opcion_actual = None

    def opcion_dict(self, texto, textos, view_name):
        subs = [{'handle': x.direccion, 'opcion': x.opcion, 'padre': x.opcion.padre_id, 'titulo': x.titulo} for x in
                filter(lambda x: x.opcion.tipo == 2 and x.opcion.padre_id == texto.opcion_id, textos)]
        es_padre = len(subs) > 0
        if texto.opcion.nombre == view_name:
            active = 'active'
            self.opcion_actual = texto.opcion
        else:
            if es_padre:
                hijo = [x for x in subs if
                        x['opcion'].nombre == view_name and x['padre'] == texto.opcion.idopcion]
                active = 'active' if len(hijo) > 0 else ''
            else:
                active = ''
        return {'handle': texto.direccion, 'titulo': texto.titulo, 'es_padre': es_padre, 'hijos': subs,
                'active': active}

    def opciones(self, idioma, view_name):
        textos = list(
            TextoOpcion.objects.filter(idioma__codigo=idioma).prefetch_related('opcion', 'opcion__padre').order_by(
                'opcion__posicion'))
        arr_opcion = [self.opcion_dict(x, textos, view_name) for x in filter(lambda x: x.opcion.tipo == 1, textos)]
        return arr_opcion
