from django.views.generic import TemplateView

from app.models import TextoOpcion


class OpcionesView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        idioma = 'en'
        textos = list(TextoOpcion.objects.filter(idioma__codigo=idioma).prefetch_related('opcion').order_by('opcion__posicion'))
        l = lambda x: {'handle': x.direccion, 'titulo': x.titulo, 'es_padre': False}
        opciones = [x.opcion for x in filter(lambda x: x.opcion.tipo == 1, textos)]
        opciones.sort(key=lambda x: x.posicion)
        # map_opcion = map({**dict_opcion, 'active': 'active' if view_name == o.nombre else '', 'es_padre': False})
        pass
