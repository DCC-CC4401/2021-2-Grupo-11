from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from Componentes.models import *
from Web.models import *


# Muestra una página con las builds mas recientes sin filtro
def index(request):
    builds = Build.objects.all()[:20]
    return render(request, "Web/index.html", {"user": request.user, "builds":builds})

# Muestra la página de busqueda de builds
def search_build(request):
    return render(request, "Web/search_build.html", {"user": request.user})

# Aqui se recibe el formulario de registro de builds y se inserta en la db
def register_build(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    elif request.method == 'GET':
        return render(request, "Web/register_build.html", {"user": request.user})
    
    elif request.method == 'POST':
        if "buildAdd" in request.POST:
            nombre = request.POST["nombre"]
            name_tarjetavideo = request.POST["tarjetavideo"]
            name_procesador = request.POST["procesador"]
            name_placamadre = request.POST["placamadre"]
            name_discohdd = request.POST["discohdd"]
            name_discossd = request.POST["discossd"]
            name_memoria = request.POST["memoria"]
            name_gabinete = request.POST["gabinete"]
            name_fuente = request.POST["fuente"]
            name_cooler = request.POST["cooler"]

            tarjetavideo = GPU.objects.get(name= name_tarjetavideo) if name_tarjetavideo != "" else None
            procesador = Procesador.objects.get(name= name_procesador)
            placamadre = PlacaMadre.objects.get(name= name_placamadre)
            memoria = RAM.objects.get(name= name_memoria)
            discohdd = DiscoDuro.objects.get(name= name_discohdd) if name_discohdd != "" else None
            discossd = SSD.objects.get(name= name_discossd) if name_discossd != "" else None
            gabinete = Gabinete.objects.get(name= name_gabinete)
            fuente = FuentePoder.objects.get(name= name_fuente)
            cooler = CoolerCPU.objects.get(name= name_cooler) if name_cooler != "" else None

            build = Build(name=nombre, usuario=request.user, procesador=procesador, tarjetavideo=tarjetavideo, placamadre=placamadre,
                            discohdd=discohdd, discossd=discossd, memoria=memoria, gabinete=gabinete, fuente=fuente, cooler=cooler)
            build.save()
            return redirect("/user")

# Aqui se muestran las builds y se pueden agregar cometarios
def details_build(request):
    if Build.objects.all().count() == 0:
        return redirect('/')

    elif request.method == 'GET':
        url_id = request.GET.get("n")

        if not url_id:
            url_id = Build.objects.first().id

        build = Build.objects.filter(id=url_id)
        comments = Comment.objects.filter(build_id=url_id).order_by('-fecha')

        return render(request, "Web/build_page.html", {"user": request.user, "build": build[0], "comments": comments})

    elif not request.user.is_authenticated:
        return redirect('/login')

    elif request.method == 'POST':
        if "commentAdd" in request.POST:
            build_id = request.POST["id"]
            text_field = request.POST["text"]

            comentario = Comment(build_id=build_id, user=request.user, content=text_field)
            comentario.save()
            
        return redirect("/details?n=" + request.POST["id"])

# Al ejecutarse, si la build es del usuario, esta se borra
def delete_build(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    url_name = request.GET.get("n")
    build = Build.objects.filter(usuario=request.user, name=url_name)

    if build:
        build.delete()

    return redirect('/user')

# Al ejecutarse, si el comentario es del usuario, esta se borra
def delete_comment(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    url_redirect = request.GET.get("id")
    url_id = request.GET.get("n")
    comment = Comment.objects.filter(user=request.user, id=url_id)

    if comment:
        comment.delete()

    if url_redirect:
        return redirect("/details?n=" + url_redirect)
    else:
        return redirect('/')

# Muestra las builds del usuario
def page_user(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    builds = Build.objects.filter(usuario=request.user).order_by('-creacion')
    return render(request, "Web/page_user.html", {"user": request.user, "builds":builds})


# Muestra la pagina de registro
def register_user(request):
    if request.user.is_authenticated:
        return redirect('user')

    elif request.method == 'GET':
        return render(request,"web/register_user.html")

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mail = request.POST['mail']
        name = request.POST['name']

        user = User.objects.create_user(username=username, password=password, email=mail, name=name)
        return redirect('/')

# Muestra la pagina de login
def login_user(request):
    if request.user.is_authenticated:
        return redirect('user')

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

# Cierra la sesion del usuario
def logout_user(request):
    logout(request)
    return redirect('/')
