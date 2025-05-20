from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("exibemensagem", views.exibe_mensagem, name="exibe_mensagem"),
<<<<<<< HEAD
    path("exibemensagemsimples", views.exibe_html_simples,
          name="exibe_mensagem_simples"),
    path("test_render",views.test_render, name="render_exibir"),
=======
    path('exibemensagensimples', views.exibe_html_simples, name="exibe_html_simples"),
    path("test_render", views.test_render,name="render_exibir"),
>>>>>>> b531f7fa8ffbad8ef919f411a5883709e336a0a9
]