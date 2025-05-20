from django.urls import path

<<<<<<< HEAD
from . import views 

urlpatterns = [
    path('exibemensagem/', views.exibe_mensagem, name="exibe_mensagem")
=======
from . import views

urlpatterns = [
    path("exibemensagem/", views.exibe_mensagem, name="exibe_mensagem"),
   
>>>>>>> b531f7fa8ffbad8ef919f411a5883709e336a0a9
]