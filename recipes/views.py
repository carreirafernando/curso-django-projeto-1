from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')
    # return HttpResponse('Pagina inicial 1')

def contato(request):
    return HttpResponse('Página de contato 1')

def sobre(request):
    return HttpResponse('Sobre 1')