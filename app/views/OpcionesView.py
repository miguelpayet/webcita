from django.views.generic import TemplateView

from app.models import Opcion


class OpcionesView(TemplateView):

    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        for o in Opcion.objects.prefetch_related().order_by('posicion'):
            pass
