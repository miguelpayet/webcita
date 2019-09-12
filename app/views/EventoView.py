from app.secciones import Foto
from app.secciones import Texto
from app.views.ViewBase import ViewBase


class EventoView(ViewBase):
    nombre_clase = 'evento'
    secciones = [Texto, Foto]
    view_name = 'Evento'

    def __init__(self):
        self.evento = None
        super().__init__()

    def get_context_data(self, **kwargs):
        self.view_name = kwargs['evento']
        return super().get_context_data()
