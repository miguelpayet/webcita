from app.secciones import Carrusel
from app.secciones import Instalacion
from app.views.MyViewBase import MyViewBase


class InstalacionesView(MyViewBase):
    nombre_clase = 'inicio'
    secciones = [Carrusel, Instalacion]
    view_name = ''


class InstalacionesCuartosView(InstalacionesView):
    view_name = 'Cuartos'


class InstalacionesAmbientesView(InstalacionesView):
    view_name = 'Ambientes'
