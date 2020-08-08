from time import time

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView

import web_app.middleware
from web_app.common import utils


class ViewBase(TemplateView):
    nombre_clase = ''
    secciones = []
    template_name = 'pagina.html'
    view_name = ''

    def __init__(self):
        self.context = {'vista': self.view_name}
        self.idioma = None
        self.pagina = None
        super().__init__()

    def datos_comunes(self):
        (self.context, self.idioma, self.pagina) = utils.datos_comunes(self.view_name)

    def get_context_data(self, **kwargs):
        self.datos_comunes()
        secciones = []
        for s in self.secciones:
            obj = s(self)
            obj(secciones)
        return self.ordenar_contexto(self.nombre_clase, secciones)

    def ordenar_contexto(self, nombre_clase, secciones):
        # sortear las secciones por posicion
        secciones = utils.sort_secciones(secciones)
        # invocar vista
        self.context.update(clase=nombre_clase, secciones=secciones)
        return self.context

    def render_to_response(self, context, **response_kwargs):
        self.request.session['django_language'] = self.idioma.codigo
        content = render_to_string(self.template_name, context, self.request)
        if hasattr(self.request, web_app.middleware.NOMBRE_LISTA):
            t = self.request.tiempos[0]
            t1 = t[web_app.middleware.NOMBRE_TIEMPO]
            content = content.replace('[tiempo]', 'render: %s seg' % (time() - t1))
        response = HttpResponse(content)
        return response
