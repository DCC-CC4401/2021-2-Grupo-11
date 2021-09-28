from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.componentes_test, name='test'),
    path('ajax',views.componentes_ajax, name='ajax'),

    
]
