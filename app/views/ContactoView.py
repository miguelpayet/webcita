from app.secciones import Carrusel
from app.secciones import Contacto
from app.views.ViewBase import ViewBase


class ContactoView(ViewBase):
    view_name = 'Contacto'
    nombre_clase = 'contacto'
    secciones = [Carrusel, Contacto]
