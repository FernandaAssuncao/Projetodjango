from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Bem vindo 2!!')


def sobre(request):
    return HttpResponse('Sobre 2!!!')


def contato(request):
    return HttpResponse('Contato 2!!!!')

