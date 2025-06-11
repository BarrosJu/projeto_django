from django.urls import path
from . import views 

app_name='titulo'

urlpatterns = [
    path('lista/', views.listar, name="listar"),
    path('cadastro/', views.cadastrar, name="cadastrar"),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('excluir/<int:codigo>', views.excluir, name="excluir_titulo"),

]