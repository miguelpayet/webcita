from app.secciones import Carrusel
from app.secciones import Texto
from app.views.ViewBase import ViewBase


class QuienesSomosView(ViewBase):
    nombre_clase = 'quienes-somos'
    secciones = [Carrusel, Texto]
    view_name = 'Quienes Somos'
