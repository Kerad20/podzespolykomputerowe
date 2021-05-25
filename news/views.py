from django.shortcuts import render, redirect
from news.models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from news.forms import ImageForm
# Create your views here.


def main(request):
    news = Wiadomosci.objects.order_by('-data')
    return render(request, 'main.html', {'news': news})


def register(request):
    if request.method == 'POST':
        imie = request.POST['imie']
        nazwisko = request.POST['nazwisko']
        nazwa = request.POST['nazwa']
        email = request.POST['email']
        haslo1 = request.POST['haslo1']
        haslo2 = request.POST['haslo2']
        if haslo1 == haslo2:
            if User.objects.filter(username=nazwa).exists():
                messages.info(request, 'Nazwa użytkownika jest już zajęta')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Użytkownik o podanym e-mailu jest już utworzony')
                return redirect('register')
            else:
                user = User.objects.create_user(username=nazwa,
                                                 first_name=imie,
                                                 last_name=nazwisko,
                                                 email=email,
                                                 password=haslo1)
                user.save()
                return redirect('log')
        else:
            messages.info(request, 'Podane hasła różnią się')
            return redirect('register')
    else:
        return render(request, 'register.html')


def log(request):
    if request.method == 'POST':
        nazwa = request.POST['nazwa']
        haslo = request.POST['haslo']
        user = auth.authenticate(username=nazwa, password=haslo)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Nieprawidłowa nazwa użytkownika lub hasło')
            return redirect('log')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        comment = request.POST['comment']
      #  image = ImageForm(request.POST, request.FILES)
        image = request.FILES['image']
        if request.user.is_authenticated:
            new = Wiadomosci.objects.create(tytul=title, tresc=comment, uzytkownik=request.user, image=image)
            new.save()
        return redirect('/')
    else:
        form = ImageForm()
        return render(request, 'add.html', {'form': form})


def profil(request):
    news = Wiadomosci.objects.all()
    return render(request, 'profil.html', {'news': news})

