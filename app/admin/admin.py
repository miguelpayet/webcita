import nested_admin
from django.contrib import admin

from app.models import FilaSeccionFoto
from app.models import FotoFilaSeccionFoto
from app.models import Idioma
from app.models import Parametro
from app.models import SeccionContacto
from app.models import SeccionFoto
from app.models import SeccionTexto
from app.models import SeccionTextoFoto
from app.models import Social
from app.models import TextoContacto
from app.models import TextoFotoFila
from app.models import TextoParametro
from app.models import TextoSeccionFoto
from app.models import TextoSeccionTexto
from app.models import TextoSeccionTextoFoto

admin.site.site_header = 'Luna Rumi'


# contacto
class TextoContactoInline(admin.StackedInline):
    model = TextoContacto
    fields = ('idioma', 'titulo', 'nombre', 'apellido', 'email', 'comentarios', 'titulo_email',)
    extra = 0


class ContactoAdmin(admin.ModelAdmin):
    fields = ('mail', 'direccion', 'telefonos', 'mapa', 'clase',)
    inlines = (TextoContactoInline,)
    list_display = ('idcontacto',)


admin.site.register(SeccionContacto, ContactoAdmin)


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


# seccion foto
class TextoFotoFilaInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'texto',)
    model = TextoFotoFila


class TextoFotoInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'titulo_superior',)
    model = TextoSeccionFoto


class FotoFilaSeccionFotoInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('imagen', 'posicion', 'destino', 'clase',)
    inlines = [TextoFotoFilaInline]
    model = FotoFilaSeccionFoto


class FilaSeccionFotoInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('posicion',)
    inlines = [FotoFilaSeccionFotoInline]
    model = FilaSeccionFoto


class SeccionFotoAdmin(nested_admin.NestedModelAdmin):
    fields = ('pagina', 'posicion', 'nombre', 'fotos', 'tipo', 'clase',)
    inlines = [TextoFotoInline, FilaSeccionFotoInline]
    list_display = ('nombre', 'posicion', 'pagina',)
    ordering = ('nombre', 'posicion',)


admin.site.register(SeccionFoto, SeccionFotoAdmin)


# seccion texto
class TextoSeccionTextoInline(admin.TabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'texto')
    model = TextoSeccionTexto


class SeccionTextoAdmin(admin.ModelAdmin):
    fields = ('pagina', 'nombre', 'posicion', 'tipo', 'clase',)
    inlines = (TextoSeccionTextoInline,)
    list_display = ('nombre', 'posicion', 'tipo',)
    ordering = ('posicion', 'nombre')


admin.site.register(SeccionTexto, SeccionTextoAdmin)


# seccion texto foto
class TextoSeccionTextoFotoInline(admin.TabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'texto',)
    model = TextoSeccionTextoFoto


class SeccionTextoFotoAdmin(admin.ModelAdmin):
    fields = (
    'pagina', 'nombre', 'posicion', 'imagen', 'imagen_menor', 'tipo', 'subtipo', 'posicion_foto', 'color', 'clase')
    inlines = (TextoSeccionTextoFotoInline,)
    list_display = ('pagina', 'posicion', 'nombre', 'tipo', 'subtipo', 'posicion_foto',)
    ordering = ('pagina', 'posicion',)


admin.site.register(SeccionTextoFoto, SeccionTextoFotoAdmin)


# social
class SocialAdmin(admin.ModelAdmin):
    fields = ('nombre', 'direccion', 'imagen', 'posicion')
    list_display = ('nombre',)
    ordering = ('nombre',)


admin.site.register(Social, SocialAdmin)
