from django.urls import path

from . import views

urlpatterns = [
    path('', views.exibe_mensagem, name="exibe_mensagem"),
   
]