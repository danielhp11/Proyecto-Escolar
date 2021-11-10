from django.db.models.query import prefetch_related_objects
from django.shortcuts import render,HttpResponse,redirect
from Ejemplo1App.models import CitaRapida,Producto
from django.core.paginator import Paginator
from Ejemplo1App.forms import FormCitaR
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def producto(request):
    #productos contiene todos los productos de la base de datos sacandolos
    #paginador tendra todos los producos de la base de datos a paginar
    producto = Producto.objects.all()    
    paginador = Paginator(producto,8)

    #recoger numero de pagians
    pagina = request.GET.get('page')
    page_production = paginador.get_page(pagina)

    return render(request,'producto.html', {'productos': page_production})


def cita_rapida(request):

    form_citaR = FormCitaR()

    return render(request, 'cita_rapida.html',{'form': form_citaR})

from Ejemplo1App.forms import RegisterForm
def registro(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form =  RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Te has registrado corectamente')
            return redirect('registro')
    
    return render(request, 'registro.html',{'register_form':register_form})

from django.contrib.auth import authenticate,login, logout

def sesion(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request, username=username,password=pwd)

        if user is not None:
            login(request,user)
            messages.success(request,'Login exitoso')
            return redirect('indexUser')
            
        else:
            messages.warning(request,'Correo o usuario invalidos')

    return render(request, 'sesion.html')

def save_citaR(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        cabello = request.POST['cabello']
        fecha = request.POST['date']
        hora = request.POST['time']
        citaR= CitaRapida(
            nombre= nombre,
            cabello= cabello,
            fecha= fecha,
            hora= hora
        )
        citaR.save()
        #Mensaje flask que se muestra solo una vez
        messages.success(request, f'Tu cita ha sido creada {nombre}')

        return redirect('cita_rapida')
    else:
        return redirect('cita_rapida')

def indexUser(request):
    return render(request,'indexUser.html')