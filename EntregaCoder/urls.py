from django.contrib import admin
from django.urls import path, include
from MyApp.views import Inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto-coder/', include('MyApp.urls')),
    path('', Inicio),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)