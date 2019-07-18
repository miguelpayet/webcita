from app.common import carrusel
from app.common import instalacion
from app.views.MyViewBase import MyViewBase


class InstalacionesView(MyViewBase):
    view_name = ''

    def get_context_data(self, **kwargs):
        # variables
        self.datos_comunes()
        # secciones
        secciones = []
        # carrusel
        carrusel(self.pagina, self.idioma, secciones)
        # instalación
        instalacion(self.__class__.view_name, self.idioma, secciones)
        return self.ordenar_contexto('instalaciones', secciones)


class InstalacionesCuartosView(InstalacionesView):
    view_name = 'Cuartos'


class InstalacionesAmbientesView(InstalacionesView):
    view_name = 'Ambientes'
