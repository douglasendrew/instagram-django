from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request, 'index/index.html')


def login_view(request):
    return render(request, 'login/login.html')


def cadastro_view(request):
    return render(request, 'login/cadastro.html')