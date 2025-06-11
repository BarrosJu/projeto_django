from django import forms

#classe formulario inclusão
class TituloForm(forms.Form):
     descricao = forms.CharField (max_length=100,
                                 required=True,
                                 help_text='Informe numero do Titulo') 