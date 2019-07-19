from app.secciones import Carrusel
from app.secciones import TextoFoto
from app.views.MyViewBase import MyViewBase


class ToursView(MyViewBase):
    view_name = 'Tours'
    nombre_clase = 'tours'
    secciones = [Carrusel, TextoFoto]
