from web_app.secciones import Foto
from web_app.secciones import Texto
from web_app.views.ViewBase import ViewBase


class RetiroView(ViewBase):
    nombre_clase = 'retiro'
    secciones = [Texto, Foto]
    view_name = 'Retiro'

    def __init__(self):
        self.retiro = None
        super().__init__()

    def get_context_data(self, **kwargs):
        retiro = kwargs['retiro']
        self.view_name = retiro
        return super().get_context_data()
