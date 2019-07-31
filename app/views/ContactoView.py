from app import models
from app.secciones import Carrusel
from app.secciones import Contacto
from app.views.ViewBase import ViewBase


class ContactoView(ViewBase):
    view_name = 'Contacto'
    nombre_clase = 'contacto'
    secciones = [Carrusel, Contacto]

    # def get(self, request, *args, **kwargs):
    #    print("hola")

    def post(self, request, *args, **kwargs):
        contacto = models.Contacto()
        contacto.nombre = request.POST['contacto_nombre']
        contacto.apellido = request.POST['contacto_apellido']
        contacto.comments = request.POST['contacto_comentarios']
        contacto.email = request.POST['contacto_email']
        contacto.save()
        return self.get(request, *args, **kwargs)
