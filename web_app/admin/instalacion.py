import nested_admin
from django.contrib import admin

from web_app.models import FotoInstalacion
from web_app.models import SeccionInstalacion
from web_app.models import TextoFotoInstalacion
from web_app.models import TextoSeccionInstalacion


class TextoFotoInstalacionInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo',)
    model = TextoFotoInstalacion


class FotoInstalacionInline(nested_admin.NestedTabularInline):
    extra = 0
    inlines = [TextoFotoInstalacionInline]  # , FotoFotoInstalacionInline
    fields = ('imagen',)
    model = FotoInstalacion


class TextoSeccionInstalacionInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'texto',)
    model = TextoSeccionInstalacion


class SeccionInstalacionAdmin(nested_admin.NestedModelAdmin):
    fields = ('pagina', 'posicion', 'nombre', 'total_fila', 'clase',)
    inlines = [TextoSeccionInstalacionInline, FotoInstalacionInline]
    list_display = ('pagina', 'nombre', 'posicion',)
    ordering = ('pagina', 'posicion',)


admin.site.register(SeccionInstalacion, SeccionInstalacionAdmin)
