import nested_admin
from django.contrib import admin

from opciones.models import Opcion
from opciones.models import TextoOpcion


class TextoOpcionInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'direccion')
    model = TextoOpcion


class OpcionAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    fields = ('pagina', 'nombre', 'tipo', 'posicion', 'idpadre',)
    inlines = (TextoOpcionInline,)
    model = Opcion
    list_display = ('nombre', 'posicion', 'tipo',)
    ordering = ('tipo', 'posicion',)


admin.site.register(Opcion, OpcionAdmin)
