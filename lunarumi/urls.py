from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from app.views import ContactoView
from app.views import EventoView
from app.views import IndexView
from app.views import InstalacionesAmbientesView
from app.views import InstalacionesCuartosView
from app.views import OpcionesView
from app.views import QuienesSomosView
from app.views import RetiroView
from app.views import ServiciosView
from app.views import ToursView

# urls de admin y django
urlpatterns = [path('admin/', admin.site.urls),
               path('i18n/', include('django.conf.urls.i18n')),
               re_path(r'^_nested_admin/', include('nested_admin.urls')),
               re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
               path('grappelli/', include('grappelli.urls')),
               ]

# urls del site
urlpatterns += i18n_patterns(
    path('', IndexView.as_view(), name='index'),
    path('contacto', ContactoView.as_view(), name="contacto"),
    path('instalaciones/ambientes', InstalacionesAmbientesView.as_view(), name="ambientes"),
    path('instalaciones/habitaciones', InstalacionesCuartosView.as_view(), name="habitaciones"),
    path('quienes-somos', QuienesSomosView.as_view(), name="quienes-somos"),
    path('servicios', ServiciosView.as_view(), name="servicios"),
    path('servicios/retiros/<retiro>', RetiroView.as_view(), name="retiros"),
    path('servicios/eventos/<evento>', EventoView.as_view(), name="eventos"),
    path('tours', ToursView.as_view(), name="tours"),
    path('opciones', OpcionesView.as_view(), name="opciones")
)
