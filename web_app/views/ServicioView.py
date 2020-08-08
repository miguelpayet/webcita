from web_app.secciones import Carrusel
from web_app.secciones import Foto
from web_app.secciones import Texto
from web_app.views.ViewBase import ViewBase


class ServiciosView(ViewBase):
    nombre_clase = 'servicios'
    secciones = [Carrusel, Texto, Foto]
    view_name = 'Servicios'

