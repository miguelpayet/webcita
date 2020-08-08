from web_app.secciones import Carrusel
from web_app.secciones import Foto
from web_app.secciones import Texto
from web_app.views.ViewBase import ViewBase


class NosotrosView(ViewBase):
    nombre_clase = 'nosotros'
    secciones = [Carrusel, Foto, Texto]
    view_name = 'Nosotros'
