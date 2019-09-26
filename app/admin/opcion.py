import nested_admin
from django.contrib import admin

from app.models import Opcion
from app.models import TextoOpcion


class TextoOpcionInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'direccion')
    model = TextoOpcion


class OpcionAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    fields = ('pagina', 'nombre', 'posicion')
    inlines = (TextoOpcionInline,)
    model = Opcion
    list_display = ('nombre', 'posicion', 'tipo', 'idpadre',)
    ordering = ('idpadre', 'posicion',)


admin.site.register(Opcion, OpcionAdmin)
