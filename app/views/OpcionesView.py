from django.views.generic import TemplateView

from app.models import Opcion


class OpcionesView(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        for o in Opcion.objects.filter(tipo=1).filter(texto__idioma__codigo='en').prefetch_related('texto').order_by('posicion'):
            pass
