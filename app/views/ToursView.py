from app.secciones import Carrusel
from app.secciones import TextoFoto
from app.views.ViewBase import ViewBase


class ToursView(ViewBase):
    view_name = 'Tours'
    nombre_clase = 'tours'
    secciones = [Carrusel, TextoFoto]
