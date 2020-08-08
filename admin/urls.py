from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from admin_app import admin_index

urlpatterns = [
    path('', admin_index, name="index"),
    path('admin/', admin.site.urls, name="admin"),
    path('grappelli/', include('grappelli.urls'), name="grappelli"),
    path(r'_nested_admin/', include('nested_admin.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]
