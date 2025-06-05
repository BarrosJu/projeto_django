from django.db import models

# Create your models here.

class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True,
                              help_text='Ente com o numero da matricula do aluno')
    nome= models.CharField(max_length=100, help_text='Informe o nome do aluno')
    data_incial = models.DateField('Informe a data de inicio do aluno')
    data_final = models.DateField('Informe a data final do aluno')

    def __str__(self):
        return f'{self.matricula} - {self.nome} - {self.data_incial} - {self.data_final}'
        
