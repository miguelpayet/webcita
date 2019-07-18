from app.common import carrusel
from app.views.MyViewBase import MyViewBase


class ContactoView(MyViewBase):
    view_name = 'Contacto'

    def get_context_data(self, **kwargs):
        self.datos_comunes()
        # secciones
        secciones = []
        # carrusel
        carrusel(self.pagina, self.idioma, secciones)
        # seccion contacto
        contactin = self.context['contacto']
        txt = contactin['texto']
        dict_contacto = {'apellido': txt.apellido, 'comentarios': txt.comentarios, 'email': txt.email, 'nombre': txt.nombre,
                         'posicion': 2, 'seccion': 'app/seccion_contacto.html', 'mapa': contactin['mapa'],
                         'titulo_email': txt.titulo_email}
        secciones.append(dict_contacto)
        return self.ordenar_contexto('contacto', secciones)
