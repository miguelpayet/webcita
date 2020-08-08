from web_app.secciones import Carrusel
from web_app.secciones import Foto
from web_app.secciones import Texto
from web_app.secciones import TextoFoto
from web_app.views.ViewBase import ViewBase


class ConsultoriaView(ViewBase):
    nombre_clase = 'consultoria'
    secciones = [Carrusel, Foto, TextoFoto, Texto]
    view_name = 'Consultoria'
