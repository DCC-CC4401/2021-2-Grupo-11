from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='web'),
    path('user',views.page_user, name='user'),
    path('build', views.register_build, name='build'),
    path('search', views.search_build, name='search'),
    path('details', views.details_build, name='details'),

    path('delete_b', views.delete_build, name='delete'),
    path('delete_c', views.delete_comment, name='delete'),
    
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    
]
