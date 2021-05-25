from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('log', views.log, name = 'log'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('add', views.add, name = 'add'),
    path('profil', views.profil, name = 'profil')
]