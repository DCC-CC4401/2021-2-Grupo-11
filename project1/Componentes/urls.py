from django.urls import path, include
from . import views


urlpatterns = [
    path('ajax',views.componentes_ajax, name='ajax'),
    
]
