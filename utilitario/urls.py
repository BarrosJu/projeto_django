from django.urls import path
from . import views 

app_name = 'utilitario'

urlpatterns = [
    path('contato/', views.cadastrar, name="cadastrar"),
    path('carga/', views.popular_bd, name='popular')
]