from web_app.secciones import Carrusel
from web_app.secciones import TextoFoto
from web_app.views.ViewBase import ViewBase


class ToursView(ViewBase):
    view_name = 'Tours'
    nombre_clase = 'tours'
    secciones = [Carrusel, TextoFoto]
