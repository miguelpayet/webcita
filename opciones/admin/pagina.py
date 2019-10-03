from opciones.models import TextoPagina
from opciones.models import Pagina

import nested_admin
from django.contrib import admin


# paginas
class TextoPaginaInline(admin.TabularInline):
    extra = 0
    fields = ('idioma', 'titulo', 'descripcion')
    model = TextoPagina


class PaginaAdmin(admin.ModelAdmin):
    fields = ('nombre',)
    inlines = (TextoPaginaInline,)
    list_display = ('nombre',)
    ordering = ('nombre',)


admin.site.register(Pagina, PaginaAdmin)
