from app.common import carrusel
from app.common.secciones import texto

from app.views.MyViewBase import MyViewBase


class QuienesSomosView(MyViewBase):
    view_name = 'Quienes Somos'

    def get_context_data(self, **kwargs):
        self.datos_comunes()
        # secciones
        secciones = []
        # carrusel
        carrusel(self.pagina, self.idioma, secciones)
        # seccion texto
        texto(self.pagina, self.idioma, secciones)
        return self.ordenar_contexto('quienes-somos', secciones)
