from app.secciones import Carrusel
from app.secciones import Foto
from app.secciones import TextoFoto
from app.views.ViewBase import ViewBase


class QuienesSomosView(ViewBase):
    nombre_clase = 'quienes-somos'
    secciones = [Carrusel, Foto, TextoFoto]
    view_name = 'Quienes Somos'
