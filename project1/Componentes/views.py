import sys
from django.shortcuts import render
from Componentes.models import *

from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

def componentes_test(request):
    pass

def componentes_ajax(request):
    if not request.user.is_authenticated:
        return HttpResponse("")

    url_comp = request.GET.get("c")
    url_name = request.GET.get("n")

    if not url_comp:
        return HttpResponse("")
    elif url_name:
        componentes = getattr(sys.modules[__name__], url_comp).objects.filter(name__icontains=url_name)[:20]
    else:
        componentes = getattr(sys.modules[__name__], url_comp).objects.all()[:20]
    
    html = render_to_string("componentes/search-partial.html", context={"componentes":componentes, "tipo":url_comp.lower()})
    data_dict = {"html_componentes": html}

    return JsonResponse(data=data_dict, safe=False)