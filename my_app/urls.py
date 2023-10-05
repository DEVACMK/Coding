from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil),
    path('akwaba', views.accueil),
    path('login', views.connexion),
]
