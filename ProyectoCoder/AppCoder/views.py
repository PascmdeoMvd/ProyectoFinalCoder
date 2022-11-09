from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import Persona
from .models import Cuidador
from .models import Mascota


# Create your views here.

def mascota(request, nombre, edad):
    
    mascota = mascota( nombre=nombre, edad=edad )
    mascota.save 
    
    return HttpResponse(f"""      
       <p>Nombre de la Mascota: {mascota.nombre} - Edad: {mascota.edad} agregado! </p>                 
""")
    




def persona(request):
    return render(request,"AppCoder/persona.html")





def Cuidador(request):
    return render(request,"AppCoder/cuidador.html")





