from django.urls import path
from .views import mascota, persona, cuidador, lista_mascotas


urlpatterns = [
    
    path('agrega-mascota/<nombre>/<edad>', mascota),
    path('lista-mascotas/', lista_mascotas),
 
    
]
    
    
       
       