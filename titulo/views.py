from django.shortcuts import HttpResponse, render

# Create your views here.

def listar(request):
    return render (request, 'titulo/listarTitulos.html')

def cadastrar(request):
    return render(request, 'titulo/cadastroTitulos.html')
