from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from Web.models import User 

def index(request):
    if request.user.is_authenticated:
        return HttpResponse("authenticated")
    else:
        return HttpResponse("uwu not found")

def register_user(request):
    if request.method == 'GET': #Si estamos cargando la página
        return HttpResponse("register_user")
        # return render(request,"web/register_user.html")

    elif request.method == 'POST': #Si estamos recibiendo el form de registro
        username = request.POST['username']
        password = request.POST['password']
        mail = request.POST['mail']
        name = request.POST['name']

        user = User.objects.create_user(username=username, password=password, email=mail, name=name)
        return HttpResponseRedirect('/')

def login_user(request):
    if request.method == 'GET': #Si estamos cargando la página
        return HttpResponse("login_user")
        # return render(request,"web/login_user.html")

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