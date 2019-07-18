from app.common import carrusel
from app.common.secciones import texto_foto
from app.views.MyViewBase import MyViewBase


class ToursView(MyViewBase):
    view_name = 'Tours'

    def get_context_data(self, **kwargs):
        self.datos_comunes()
        # secciones
        secciones = []
        # carrusel
        carrusel(self.pagina, self.idioma, secciones)
        # seccion texto
        texto_foto(self.pagina, self.idioma, secciones)
        return self.ordenar_contexto('tours', secciones)
