from django.db import models

# Create your models here.
class Atividade(models.Model):
    lista_prioridades = (
        ('0','Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente'),
    )
    lista_status = (
        ('0', 'Pendente'),
        ('1', 'Realizando'),
        ('2', 'Concluído'),
    )

    date = models.DateField()
    atividade = models.CharField(max_length=80)
    prioridade = models.CharField(max_length=1,choices=lista_prioridades)
    contratante = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=20)
    status = models.CharField(max_length=1,choices=lista_status)

    def __str__(self):
        return self.atividade