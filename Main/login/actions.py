from django.shortcuts import render, redirect
from Main.models import Usuarios
from django.contrib import messages
from django.http.response import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def new_account(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if Usuarios.objects.filter(email=email).exists():
            messages.error(request, 'Email em uso')
            return redirect('/singup/')
        else:
            Usuarios.objects.create(nome=nome,email=email,senha=senha,is_instagram_admin=0)

            user = User.objects.create_user(email,email,senha)
            user.first_name = nome
            user.save()

            return redirect('/login/')

    else:
        raise Http404()


def make_login(request):
    
    if request.method == 'POST':
        email= request.POST.get('email')
        senha= request.POST.get('senha')

        usuario = authenticate(username=email, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Email ou senha incorreto')
            return redirect('/login/')
    else:
        raise Http404()
    

def logout_user(request):
    logout(request)
    return redirect('/')