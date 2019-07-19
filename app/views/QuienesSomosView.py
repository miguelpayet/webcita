from app.secciones import Carrusel
from app.secciones import Texto
from app.views.MyViewBase import MyViewBase


class QuienesSomosView(MyViewBase):
    nombre_clase = 'quienes-somos'
    secciones = [Carrusel, Texto]
    view_name = 'Quienes Somos'
