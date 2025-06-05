from django.db import models

# Create your models here.
class Turmas(models.Model):
    numero = models.AutoField(primary_key=True, help_text='Infome o numero da turma')
    horarioAula = models.TimeField( help_text='Informe o RG do Instrutor')
    duracaoAula = models.SmallIntegerField( help_text=' Informe o nome do instrutor')
    dataInicial = models.DateField (help_text='Informe a data de inicio das aulas')
    dataFinal= models.DateField( help_text='Informe a data final da aulas')
   
   
    def __str__(self):
        return f'{self.numero} - {self.horarioAula} - {self.duracaoAula} - {self.dataInicial} - {self.dataFinal}'
        

