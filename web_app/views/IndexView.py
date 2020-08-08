from web_app.secciones import Carrusel
from web_app.secciones import Foto
from web_app.secciones import TextoFoto
from web_app.views.ViewBase import ViewBase


class IndexView(ViewBase):
    nombre_clase = 'inicio'
    secciones = [Carrusel, TextoFoto, Foto]
    view_name = 'Inicio'
