from django.shortcuts import render, HttpResponse
from .models import Auto
from .forms import BusquedaPatente


# Create your views here.
"""""
def busqueda(request):
    if request.method == "POST":
        buscar = request.POST['buscar']
        return render(request,"core/home.html",{'buscar':buscar})    
        #id=data
        #autos = Auto.objects.get(patente=id)
    else:
        return render(request,"core/home.html",{})
"""

def home(request):
    busqueda_patente = BusquedaPatente()
    
    
    if request.method == "POST":
        busqueda_patente=BusquedaPatente(data=request.POST)
        if busqueda_patente.is_valid():
            consulta_patente = request.POST.get('patente','')
            autos = Auto.objects.filter(patente=consulta_patente)

            if len(autos)==0:
                return render(request,"core/error.html", {'form': busqueda_patente})

            else:
                return render(request,"core/consulta.html", {'autos': autos})
    
    return render(request,"core/home.html", {'form': busqueda_patente})


