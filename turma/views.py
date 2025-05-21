from django.shortcuts import HttpResponse

# Create your views here.
def exibe_mensagem(request):
  return HttpResponse("Página da Turma")
