from django.contrib import admin
from django.urls import path, include
from .views import mascota, persona, cuidador


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-mascota/<nombre>/<edad>', mascota),
    
    
]

