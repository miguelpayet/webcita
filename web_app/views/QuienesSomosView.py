from web_app.secciones import Carrusel
from web_app.secciones import Foto
from web_app.secciones import TextoFoto
from web_app.views.ViewBase import ViewBase


class QuienesSomosView(ViewBase):
    nombre_clase = 'quienes-somos'
    secciones = [Carrusel, Foto, TextoFoto]
    view_name = 'Quienes Somos'
