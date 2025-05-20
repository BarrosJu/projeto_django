from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return HttpResponse("Olá eu sou index")

def exibe_mensagem(request):
    t_html = '<html><body>Hello</body></html>'
    return HttpResponse(t_html)

def exibe_html_simples(request):
<<<<<<< HEAD
    t_html = '<html><body>Ola<body><html>'
    return HttpResponse(t_html)

def test_render(request):
    return render(request, 'escola.hmtl')
=======
    t_html = '<html><body>Hello</body></html>'
    return HttpResponse(t_html)

def test_render(request):
    return render(request, 'index.html')    
>>>>>>> b531f7fa8ffbad8ef919f411a5883709e336a0a9
