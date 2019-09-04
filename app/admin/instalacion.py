import nested_admin
from django.contrib import admin

from app.models import FotoInstalacion
from app.models import SeccionInstalacion
from app.models import TextoFotoInstalacion
from app.models import TextoSeccionInstalacion


# class FotoFotoInstalacionInline(nested_admin.NestedTabularInline):
#     extra = 0
#     fields = ('imagen', 'idfoto', 'foto',)
#     model = FotoFotoInstalacion


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
