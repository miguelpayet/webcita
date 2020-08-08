import nested_admin
from django.contrib import admin

from web_app.models import ImagenSeccionCarrusel
from web_app.models import SeccionCarrusel
from web_app.models import TextoImagenSeccionCarrusel
from web_app.models import TextoSeccionCarrusel


# sección carrusel
class TextoImagenSeccionCarruselInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'texto', 'imagen',)
    model = TextoImagenSeccionCarrusel


class TextoSeccionCarruselInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo',)
    model = TextoSeccionCarrusel


class ImagenSeccionCarruselAdmin(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('imagen', 'destino', 'posicion', 'posx', 'posy', 'ancho', 'color')
    inlines = [TextoImagenSeccionCarruselInline]
    list_display = ('posicion', 'imagen',)
    model = ImagenSeccionCarrusel


class SeccionCarruselAdmin(nested_admin.NestedModelAdmin):
    fields = ('pagina', 'posicion', 'nombre', 'fotosfila', 'tipo', 'clase')
    inlines = [TextoSeccionCarruselInline, ImagenSeccionCarruselAdmin]
    list_display = ('pagina', 'nombre', 'posicion', 'tipo',)
    ordering = ('pagina', 'posicion',)


admin.site.register(SeccionCarrusel, SeccionCarruselAdmin)
