from django.urls import path, include
from . import views


urlpatterns = [
    path('comps',views.componentes_ajax, name='componentes'),
    path('build',views.build_ajax, name='builds'),
    
]
