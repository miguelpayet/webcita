from app.secciones import Carrusel
from app.secciones import Foto
from app.secciones import TextoFoto
from app.views.ViewBase import ViewBase


class IndexView(ViewBase):
    nombre_clase = 'inicio'
    secciones = [Carrusel, TextoFoto, Foto]
    view_name = 'Inicio'
