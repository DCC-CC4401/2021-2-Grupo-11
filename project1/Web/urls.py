from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='web'),
    path('user',views.page_user, name='user'),
    path('delete', views.delete_build, name='build'),
    path('build', views.register_build, name='build'),
    path('build_page', views.build_page, name='b'),
    
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),

    
]
