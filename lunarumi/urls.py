from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from app.views import contacto
from app.views import index
from app.views import instalaciones_ambientes
from app.views import instalaciones_cuartos
from app.views import quienes_somos
from app.views import servicios
from app.views import tours
from app.views.InstalacionDetalle import InstalacionDetalle

# admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    re_path(r'ajax/detalle_foto/(?P<id>.*)$', InstalacionDetalle.as_view(), name='instalación_detalle'),
    re_path(r'^_nested_admin/', include('nested_admin.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]

# site
urlpatterns += i18n_patterns(
    path('', index, name='index'),
    path('contacto', contacto, name="contacto"),
    path('instalaciones/ambientes', instalaciones_ambientes, name="ambientes"),
    path('instalaciones/cuartos', instalaciones_cuartos, name="cuartos"),
    path('quienes-somos', quienes_somos, name="quienes-somos"),
    path('servicios', servicios, name="servicios"),
    path('tours', tours, name="tours"),
)
