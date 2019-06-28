import nested_admin
from django.contrib import admin

from app.models import ImagenSeccionCarrusel
from app.models import SeccionCarrusel
from app.models import TextoImagenSeccionCarrusel
from app.models import TextoSeccionCarrusel


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
    fields = ('imagen', 'posicion', 'posx', 'posy', 'ancho', 'color')
    inlines = [TextoImagenSeccionCarruselInline]
    list_display = ('posicion', 'imagen',)
    model = ImagenSeccionCarrusel


class SeccionCarruselAdmin(nested_admin.NestedModelAdmin):
    fields = ('pagina', 'posicion', 'nombre', 'fotosfila', 'tipo')
    inlines = [TextoSeccionCarruselInline, ImagenSeccionCarruselAdmin]
    list_display = ('pagina', 'nombre', 'posicion',)
    ordering = ('pagina', 'posicion',)


admin.site.register(SeccionCarrusel, SeccionCarruselAdmin)
