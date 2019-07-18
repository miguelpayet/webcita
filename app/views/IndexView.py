from app.common import carrusel
from app.common import foto
from app.common import texto_foto
from app.views.MyViewBase import MyViewBase


class IndexView(MyViewBase):
    view_name = 'Inicio'

    def get_context_data(self, **kwargs):
        self.datos_comunes()
        # secciones
        secciones = []
        # carrusel
        carrusel(self.pagina, self.idioma, secciones)
        # texto foto
        texto_foto(self.pagina, self.idioma, secciones)
        # foto
        foto(IndexView.view_name, self.idioma, secciones)
        return self.ordenar_contexto('inicio', secciones)
