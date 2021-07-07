from django.shortcuts import render, redirect
from .models import Registro
from .forms import RegistroForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def ver_registros(request):
    registro = Registro.objects.all()

    return render(request, 'core/ver_registros.html',context={'registro': registro})

def registrar(request):
    if request.method=='POST':
        registro = RegistroForm(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect('index')
    else:
        registro = RegistroForm()
    return render(request,'core/registrar.html', {'registro': registro})


def modificar(request,id):
    registro = Registro.objects.get(numIdentificacion=id)
    datos = {
        'form': RegistroForm(instance=registro)
    }
    if request.method=='POST':
        formulario = RegistroForm(data=request.POST, instance = registro)
        if formulario.is_valid():
            formulario.save()
            return redirect('ver_registros')

    return render(request, 'core/modificar.html', datos)

def eliminar(request,id):
    registro = Registro.objects.get(numIdentificacion=id)
    registro.delete()
    return redirect('ver_registros')