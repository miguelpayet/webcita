from django.shortcuts import render
from django.views.generic import TemplateView

from web_app.models import Pagina


class ArbolView(TemplateView):

    def get_context_data(self, **kwargs):
        context = {}
        lst_paginas = []
        for p in Pagina.objects.all():
            lst_secciones = []
            lst_secciones += list(p.seccionfoto_set.all())
            lst_secciones += list(p.seccioninstalacion_set.all())
            lst_secciones += list(p.secciontexto_set.all())
            lst_secciones += list(p.secciontextofoto_set.all())
            lst_secciones += list(p.seccioncarrusel_set.all())
            lst_secciones.sort(key=lambda x: x.posicion)
            lst_secc_pagina = []
            for s in lst_secciones:
                lst_secc_pagina.append({'nombre': s.nombre, 'posicion': s.posicion, 'tipo': s.__class__.__name__})
            lst_paginas.append({'nombre': p.nombre, 'secciones': lst_secc_pagina})
        context.update({'paginas': lst_paginas})
        return context

    def render_to_response(self, context, **response_kwargs):
        return render(self.request, "arbol.html", context)
