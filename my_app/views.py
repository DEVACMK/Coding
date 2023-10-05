from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def connexion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.info(request, "Nom utilisateur ou mot de passe incorrecte")

        print(username)
        print(password)
    return render(request, "utilisateur/login.html")

def accueil(request):
    return render(request, "utilisateur/index.html")
