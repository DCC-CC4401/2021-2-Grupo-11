from django.urls import path, include
from . import views


urlpatterns = [
    path('comps',views.componentes_ajax, name='componentes'),
    path('build',views.componentes_ajax, name='builds'),
    
]
