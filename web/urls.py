from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from web_app.views import ArbolView
from web_app.views import ConsultoriaView
from web_app.views import ContactoView
from web_app.views import IndexView
from web_app.views import NosotrosView

# urls de admin y django
urlpatterns = [path('i18n/', include('django.conf.urls.i18n')),
               re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
               ]

# opciones = Opcion.objects.all()
# for o in opciones:
#    urlpatterns += path(o.direccion,

# urls del site
urlpatterns += i18n_patterns(
    path('arbol', ArbolView.as_view(), name='arbol'),
    path('', IndexView.as_view(), name='index1'),
    path('inicio', IndexView.as_view(), name='index2'),
    path('nosotros', NosotrosView.as_view(), name="nosotros"),
    path('contacto', ContactoView.as_view(), name="contacto"),
    path('consultoria', ConsultoriaView.as_view(), name="habitaciones"),

)
