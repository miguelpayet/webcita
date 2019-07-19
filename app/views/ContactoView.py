from app.secciones import Carrusel
from app.secciones import Contacto
from app.views.MyViewBase import MyViewBase


class ContactoView(MyViewBase):
    view_name = 'Contacto'
    nombre_clase = 'inicio'
    secciones = [Carrusel, Contacto]
