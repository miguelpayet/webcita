import nested_admin
from django.contrib import admin

from app.models import Opcion
from app.models import SubOpcion
from app.models import TextoDatoOpcion
from app.models import DatoOpcion


class TextoDatoInline(nested_admin.NestedTabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'direccion')
    model = TextoDatoOpcion


class DatoOpcionAdmin(nested_admin.NestedModelAdmin):
    extra = 0
    fields = ('pagina', 'nombre', 'posicion')
    inlines = (TextoDatoInline,)
    model = DatoOpcion
    list_display = ('nombre', 'posicion',)
    ordering = ('posicion',)


admin.site.register(DatoOpcion, DatoOpcionAdmin)

# class SubOpcionInline(nested_admin.NestedTabularInline):
#     extra = 0
#     inlines = (DatoOpcionInline,)
#     model = SubOpcion
#
#
# class OpcionAdmin(nested_admin.NestedModelAdmin):
#     inlines = (DatoOpcionInline, SubOpcionInline)
#
#
# admin.site.register(Opcion, OpcionAdmin)
