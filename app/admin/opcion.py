import nested_admin
from django.contrib import admin

from app.models import Opcion
from app.models import SubOpcion
from app.models import TextoOpcion
from app.models import TextoSubOpcion


class TextoSubOpcionInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'direccion')
    model = TextoSubOpcion


class SubOpcionInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('pagina', 'nombre', 'posicion',)
    inlines = (TextoSubOpcionInline,)
    model = SubOpcion


class TextoOpcionInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'direccion')
    model = TextoOpcion


class OpcionAdmin(nested_admin.NestedModelAdmin):
    fields = ('pagina', 'posicion', 'nombre',)
    inlines = (TextoOpcionInline, SubOpcionInline)
    list_display = ('nombre', 'posicion',)
    ordering = ('posicion',)


admin.site.register(Opcion, OpcionAdmin)
