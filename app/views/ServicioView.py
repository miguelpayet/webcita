from app.secciones import Carrusel
from app.secciones import Foto
from app.secciones import Texto
from app.views.ViewBase import ViewBase


class ServiciosView(ViewBase):
    nombre_clase = 'servicios'
    secciones = [Carrusel, Texto, Foto]
    view_name = 'Servicios'
