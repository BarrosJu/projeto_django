from django.shortcuts import HttpResponse

# Create your views here.
def exibe_mensagem(request):
<<<<<<< HEAD
    return HttpResponse("Página da Turma")
=======
    t_html = '<html><body>Turma!</body></html>'
    return HttpResponse(t_html)
>>>>>>> b531f7fa8ffbad8ef919f411a5883709e336a0a9
