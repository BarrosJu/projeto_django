from django.shortcuts import HttpResponse

# Create your views here.
<<<<<<< HEAD

def exibe_mensagem(request):
    return HttpResponse("Página do aluno")

=======
def exibe_mensagem(request):
    t_html = '<html><body>Hello Student!</body></html>'
    return HttpResponse(t_html)
>>>>>>> b531f7fa8ffbad8ef919f411a5883709e336a0a9
