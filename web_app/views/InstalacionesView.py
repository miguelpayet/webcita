from web_app.secciones import Carrusel
from web_app.secciones import Instalacion
from web_app.views.ViewBase import ViewBase


class InstalacionesView(ViewBase):
    nombre_clase = ''
    secciones = [Carrusel, Instalacion]
    view_name = ''


class InstalacionesCuartosView(InstalacionesView):
    nombre_clase = 'cuartos'
    view_name = 'Habitaciones'


class InstalacionesAmbientesView(InstalacionesView):
    nombre_clase = 'ambientes'
    view_name = 'Ambientes'
