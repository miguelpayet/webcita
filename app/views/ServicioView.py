from app.secciones import Carrusel
from app.secciones import Foto
from app.secciones import Texto
from app.views.MyViewBase import MyViewBase


class ServiciosView(MyViewBase):
    nombre_clase = 'servicios'
    secciones = [Carrusel, Texto, Foto]
    view_name = 'Servicios'
