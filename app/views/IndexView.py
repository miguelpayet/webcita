from app.secciones import Carrusel
from app.secciones import Foto
from app.secciones import TextoFoto
from app.views.MyViewBase import MyViewBase


class IndexView(MyViewBase):
    nombre_clase = 'inicio'
    secciones = [Carrusel, TextoFoto, Foto]
    view_name = 'Inicio'
