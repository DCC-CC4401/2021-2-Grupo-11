from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from Componentes.models import *
from django.contrib import messages
from Web.models import User

def index(request):
    return render(request, "Web/index.html")


def register_build(request):
    if request.method == 'GET':
        procesador = Procesador.objects.all()
        tarjetavideo = GPU.objects.all()
        placamadre = PlacaMadre.objects.all()
        disco0 = Almacenamiento.objects.all()
        memoria = RAM.objects.all()
        gabinete = Gabinete.objects.all()
        fuente = FuentePoder.objects.all()
        cooler = CoolerCPU.objects.all()
        componentes = {"procesador": procesador, "tarjetavideo": tarjetavideo, "placamadre": placamadre,
            "disco0": disco0, "memoria": memoria, "gabinete": gabinete, "fuente": fuente, "cooler": cooler}

        return render(request, "Web/register_build.html", componentes)
    
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/register')
        
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
        return HttpResponseRedirect('/login')
    
    return render(request, "Web/page_user.html")


def register_user(request):
    if request.method == 'GET':
        return render(request,"web/register_user.html")

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mail = request.POST['mail']
        name = request.POST['name']

        user = User.objects.create_user(username=username, password=password, email=mail, name=name)
        return HttpResponseRedirect('/')


def login_user(request):
    if request.method == 'GET':
        return render(request,"web/login_user.html")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/register')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

