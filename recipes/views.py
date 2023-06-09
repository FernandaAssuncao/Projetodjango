from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html')


def sobre(request):
    return HttpResponse('Sobre 2!!!')


def contato(request):
    return HttpResponse('Contato 2!!!!')

