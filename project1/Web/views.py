from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from Componentes.models import *
from Web.models import User

def index(request):
    return render(request, "Web/index.html")


def register_build(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    elif request.method == 'GET':
        procesador = Procesador.objects.all()
        tarjetavideo = GPU.objects.all()
        placamadre = PlacaMadre.objects.all()
        memoria = RAM.objects.all()
        gabinete = Gabinete.objects.all()
        fuente = FuentePoder.objects.all()
        cooler = CoolerCPU.objects.all()
        componentes = {"procesador": procesador, "tarjetavideo": tarjetavideo, "placamadre": placamadre,
                       "memoria": memoria, "gabinete": gabinete, "fuente": fuente, "cooler": cooler}

        return render(request, "Web/register_build.html", componentes)
    
    elif request.method == 'POST':
        if "buildAdd" in request.POST:
            name_procesador = request.POST["procesador"]
            name_tarjetavideo = request.POST["tarjetavideo"]
            name_placamadre = request.POST["placamadre"]
            name_disco0 = request.POST["disco0"]
            name_memoria = request.POST["memoria"]
            name_gabinete = request.POST["gabinete"]
            name_fuente = request.POST["fuente"]
            name_cooler = request.POST["cooler"]

            procesador = Procesador.objects.get(name= name_procesador)
            tarjetavideo = GPU.objects.get(name= name_tarjetavideo)
            placamadre = PlacaMadre.objects.get(name= name_placamadre)
            disco0 = Almacenamiento.objects.get(name= name_disco0)
            memoria = RAM.objects.get(name= name_memoria)
            gabinete = Gabinete.objects.get(name= name_gabinete)
            fuente = FuentePoder.objects.get(name= name_fuente)
            cooler = CoolerCPU.objects.get(name= name_cooler)

            build = Build(procesador= procesador, tarjetavideo= tarjetavideo, placamadre= placamadre,
                disco0= disco0, memoria= memoria, gabinete= gabinete, fuente= fuente, cooler= cooler)
            build.save()
            return redirect("/user")


def page_user(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    builds = Build.objects.filter(usuario=request.user)
    return render(request, "Web/page_user.html", {"user": request.user, "builds":builds})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    elif request.method == 'GET':
        return render(request,"web/register_user.html")

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mail = request.POST['mail']
        name = request.POST['name']

        user = User.objects.create_user(username=username, password=password, email=mail, name=name)
        return redirect('/')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        return render(request,"web/login_user.html")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            return redirect('/register')


def logout_user(request):
    logout(request)
    return redirect('/')

