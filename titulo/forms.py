from django import forms

#classe formulario inclusão
class TituloForm(forms.Form):
     descricao = forms.CharField (max_length=100,
                                 required=True,
                                 help_text='Informe numero do Titulo') 
     
class TituloAtualizarForm(forms.Form):
     codigo = forms.IntegerField(required=True, 
                              help_text='Código dos titulos')
     descricao = forms.CharField (max_length=100,
                                 required=True,
                                 help_text='Informe numero do Titulo') 
