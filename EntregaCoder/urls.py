from django.contrib import admin
from django.urls import path, include
from MyApp.views import Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto-coder/', include('MyApp.urls')),
    path('', Inicio),
]