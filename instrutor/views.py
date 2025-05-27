from django.shortcuts import HttpResponse, render

# Create your views here.

def listar(request):
    return render(request, 'instrutor/listarInstrutores.html')

def cadastrar(request):
    return render(request,'instrutor/cadastroInstrutor.html')

