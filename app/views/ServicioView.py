from app.common import carrusel
from app.common.seccion_foto import foto
from app.common.secciones import texto
from app.views.MyViewBase import MyViewBase


class ServiciosView(MyViewBase):
    view_name = 'Servicios'

    def get_context_data(self, **kwargs):
        self.datos_comunes()
        # secciones
        secciones = []
        # carrusel
        carrusel(self.pagina, self.idioma, secciones)
        # seccion texto
        texto(self.pagina, self.idioma, secciones)
        # seccion foto
        foto(ServiciosView.view_name, self.idioma, secciones)
        return self.ordenar_contexto('servicios', secciones)
