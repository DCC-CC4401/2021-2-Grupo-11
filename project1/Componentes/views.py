from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render
import sys

from Componentes.models import *


def componentes_ajax(request):
    if not request.user.is_authenticated or not request.is_ajax():
        return JsonResponse(data={"html_componentes": "<option value='No se encontraron resultados'>"}, safe=False)

    url_comp = request.GET.get("c")
    url_name = request.GET.get("n")
    url_mode = request.GET.get("m")

    allow = {"GPU","Procesador","PlacaMadre","RAM","DiscoDuro","SSD","Gabinete","FuentePoder",
                "CoolerCPU","Mouse","Teclado","Monitor","Audifonos","SillaGamer"}

    if not url_comp or not url_comp in allow:
        return JsonResponse(data={"html_componentes": "<option value='No se encontraron resultados'>"}, safe=False)
    
    if url_mode:
        url = "componentes/details_componentes.html"
    else:
        url = "componentes/search_componentes.html"
    
    if url_name:
        componentes = getattr(sys.modules[__name__], url_comp).objects.filter(name__icontains=url_name)[:20]
    else:
        componentes = getattr(sys.modules[__name__], url_comp).objects.all()[:20]
    
    html = render_to_string(url, context={"componentes":componentes})
    data_dict = {"html_response": html}

    return JsonResponse(data=data_dict, safe=False)


def build_ajax(request):
    #if not request.is_ajax():
    #    return JsonResponse(data={"html_componentes": "<option value='No se encontraron resultados'>"}, safe=False)
    
    url_user = request.GET.get("u")
    url_page = request.GET.get("p")

    if not url_page:
        page = 0
    else:
        page = url_page * 20

    if url_user:
        builds = Build.objects.filter(usuario=request.user).order_by('-creacion')[int(page):int(page)+20]
    else:
        builds = Build.objects.all()[int(page):int(page)+20]

    html = render_to_string("componentes/details_builds.html", context={"user":request.user, "builds":builds})
    data_dict = {"html_response": html}
    
    return JsonResponse(data=data_dict, safe=False)
