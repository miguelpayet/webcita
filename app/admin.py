import nested_admin
from django.contrib import admin

from app.models import Contacto
from app.models import FilaSeccionFoto
from app.models import FotoFilaSeccionFoto
from app.models import Idioma
from app.models import ImagenSeccionCarrusel
from app.models import Opcion
from app.models import Parametro
from app.models import SeccionCarrusel
from app.models import SeccionFoto
from app.models import SeccionTexto
from app.models import SeccionTextoFoto
from app.models import Social
from app.models import TextoContacto
from app.models import TextoFotoFila
from app.models import TextoImagenSeccionCarrusel
from app.models import TextoOpcion
from app.models import TextoParametro
from app.models import TextoSeccionCarrusel
from app.models import TextoSeccionFoto
from app.models import TextoSeccionTexto
from app.models import TextoSeccionTextoFoto


# contacto
class TextoContactoInline(admin.TabularInline):
    model = TextoContacto
    fields = ('idioma', 'titulo',)
    extra = 0


class ContactoAdmin(admin.ModelAdmin):
    fields = ('mail', 'direccion', 'telefonos',)
    inlines = (TextoContactoInline,)
    list_display = ('idcontacto',)


admin.site.register(Contacto, ContactoAdmin)


# idioma
class IdiomaAdmin(admin.ModelAdmin):
    fields = ('codigo', 'nombre', 'imagen')
    list_display = ('codigo', 'nombre',)


admin.site.register(Idioma, IdiomaAdmin)


# parametros
class TextoParametroInline(admin.TabularInline):
    model = TextoParametro
    fields = ('idioma', 'copyright', 'titulosocial')
    extra = 0


class ParametroAdmin(admin.ModelAdmin):
    fields = ('logoblanco', 'logomarron',)
    inlines = (TextoParametroInline,)
    list_display = ('idparametro',)


admin.site.register(Parametro, ParametroAdmin)


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
    extra = 0
    fields = ('opcion', 'nombre', 'posicion', 'fotosfila', 'tipo')
    inlines = [TextoSeccionCarruselInline, ImagenSeccionCarruselAdmin]
    list_display = ('opcion', 'nombre', 'posicion',)
    ordering = ('opcion', 'posicion',)


admin.site.register(SeccionCarrusel, SeccionCarruselAdmin)


# seccion foto
class TextoFotoFilaInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'texto',)
    model = TextoFotoFila


class TextoFotoInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo',)
    model = TextoSeccionFoto


class FotoFilaSeccionFotoInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('imagen', 'posicion',)
    inlines = [TextoFotoFilaInline]
    model = FotoFilaSeccionFoto


class FilaSeccionFotoInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('posicion',)
    inlines = [FotoFilaSeccionFotoInline]
    model = FilaSeccionFoto


class SeccionFotoAdmin(nested_admin.NestedModelAdmin):
    fields = ('nombre', 'opcion', 'posicion',)
    inlines = [TextoFotoInline, FilaSeccionFotoInline]
    list_display = ('opcion', 'posicion', 'nombre',)
    ordering = ('opcion', 'posicion',)


admin.site.register(SeccionFoto, SeccionFotoAdmin)


# seccion texto
class TextoSeccionTextoInline(admin.TabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'texto')
    model = TextoSeccionTexto


class SeccionTextoAdmin(admin.ModelAdmin):
    fields = ('opcion', 'nombre', 'posicion')
    inlines = (TextoSeccionTextoInline,)
    list_display = ('nombre', 'posicion')
    ordering = ('posicion', 'nombre')


admin.site.register(SeccionTexto, SeccionTextoAdmin)


# seccion texto foto
class TextoSeccionTextoFotoInline(admin.TabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'texto',)
    model = TextoSeccionTextoFoto


class SeccionTextoFotoAdmin(admin.ModelAdmin):
    fields = ('imagen', 'nombre', 'opcion', 'posicion', 'tipo', 'color')
    inlines = (TextoSeccionTextoFotoInline,)
    list_display = ('opcion', 'posicion', 'nombre')
    ordering = ('opcion', 'posicion',)


admin.site.register(SeccionTextoFoto, SeccionTextoFotoAdmin)


# sección texto imagen
class OpcionTextoInline(admin.TabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'direccion')
    model = TextoOpcion


class OpcionAdmin(admin.ModelAdmin):
    fields = ('posicion', 'nombre',)
    inlines = (OpcionTextoInline,)
    list_display = ('nombre', 'posicion',)
    ordering = ('posicion',)


admin.site.register(Opcion, OpcionAdmin)


# social
class SocialAdmin(admin.ModelAdmin):
    fields = ('nombre', 'direccion', 'imagen', 'posicion')
    list_display = ('nombre',)
    ordering = ('nombre',)


admin.site.register(Social, SocialAdmin)
