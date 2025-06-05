from django.db import models

# Create your models here.

class Instrutor(models.Model):
    id = models.AutoField(primary_key=True, help_text='Infome o ID do instrutor')
    rg = models.CharField(max_length=15, help_text='Informe o RG do Instrutor')
    nome = models.CharField(max_length=70, help_text=' Informe o nome do instrutor')
    data_Nascimento = models.DateField ('Informe a data de nascimento')
    telefone = models.CharField(max_length=9, help_text='Informe o número de telefone')
    ddd = models.CharField(max_length=3, help_text='Informe o DDD')


    def __str__(self):
        return f'{self.id} - {self.rg} - {self.nome} - {self.data_Nascimento} - {self.telefone} - {self.ddd}'
        


 