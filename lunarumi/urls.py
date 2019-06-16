from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from app.views import contacto
from app.views import index
from app.views import instalaciones
from app.views import quienes_somos
from app.views import servicios
from app.views import tours

# admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    re_path(r'^_nested_admin/', include('nested_admin.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]

# site
urlpatterns += i18n_patterns(
    path('', index, name='index'),
    path('quienes-somos', quienes_somos, name="quienes-somos"),
    path('instalaciones', instalaciones, name="instalaciones"),
    path('tours', tours, name="tours"),
    path('servicios', servicios, name="servicios"),
    path('contacto', contacto, name="contacto"),
)
