from app.secciones import Foto
from app.secciones import Texto
from app.views.ViewBase import ViewBase


class DetalleRetiroView(ViewBase):
    nombre_clase = 'detalle-retiro'
    secciones = [Texto, Foto]
    view_name = 'DetalleRetiro'

    def __init__(self):
        self.retiro = None
        super().__init__()

    def get_context_data(self, **kwargs):
        retiro = kwargs['retiro']
        self.view_name = '%s-detalle' % retiro
        return super().get_context_data()
