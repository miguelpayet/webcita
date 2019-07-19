from .SeccionBase import SeccionBase


# todo: la posición está en duro

class Contacto(SeccionBase):
    template_seccion = 'seccion_contacto.html'

    def __call__(self, secciones):
        contacto = self.vista.context['contacto']
        txt = contacto['texto']
        dict_contacto = {'apellido': txt.apellido, 'comentarios': txt.comentarios, 'email': txt.email, 'nombre': txt.nombre,
                         'posicion': 2, 'seccion': self.template_seccion, 'mapa': contacto['mapa'],
                         'titulo_email': txt.titulo_email}
        secciones.append(dict_contacto)
