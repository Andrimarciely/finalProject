from django.db import models


class Matrix(models.Model):
    description = models.CharField(
        help_text="nome da matriz",
        max_length=200,
        verbose_name="matriz"
    )
    def __str__(self):
        return self.description


class OtherDocuments(models.Model):
    registration_number = models.CharField(
        help_text="número de inscrição",
        max_length=50,
        verbose_name="número de inscrição",
    )
    description = models.CharField(
        help_text="nome da autarquia",
        max_length=200,
        verbose_name="nome da autarquia"
    )

class Company(models.Model):
    class Meta:
        abstract = True

    corporate_name = models.CharField(
        help_text="razão social da empresa contratada",
        max_length=200,
        verbose_name="Razão Social",
    )
    address = models.CharField(
        help_text="endereço da empresa contratada",
        max_length=200,
        verbose_name="Endereço",
    )
    phone_fax = models.CharField(
            help_text="telefone para contato",
            max_length=50,
            verbose_name="Telefone/Fax",
    )
    cnpj = models.CharField(
        blank=True,
        max_length=50,
        verbose_name=("CNPJ"),
        help_text=("CNPJ"),
    )

'''The Contracted Company - The appraisal company - ACME '''
class EnvironmentalConsultancy(Company):
    other_documents = models.ForeignKey(
        OtherDocuments,
        on_delete=models.CASCADE,
        verbose_name="Outros Documentos (licenças, registros e afins)"
    )
    def __str__(self):
        return self.corporate_name


'''The Contracting Company - The appraised company '''
class Client(Company):
    email = models.EmailField(
        blank=True,
        help_text="endereço e-Mail",
        max_length=254,
        null=True,
        verbose_name="endereço e-Mail",
    )
    responsible_contact=models.CharField(
        help_text="Nome do Responsável Técnico",
        max_length=80,
        verbose_name="nome do responsável técnico",
    )
    def __str__(self):
        return self.corporate_name

class Event(models.Model):
    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', "Muito Urgente"),
    )

    inital_date = models.DateField(
        help_text="data inicial",
    )
    final_date = models.DateField(
        help_text="data final",
    )
    responsible_technician = models.CharField(
        help_text="responsável técnico",
        max_length=80,
        verbose_name="técnico",
    )
    description = models.CharField(
        help_text="visita, coleta, ou relatório?",
        max_length=100,
        verbose_name="descrição",
    )
    priority = models.CharField(
        max_length=1,
        choices=priorities_list,
        verbose_name="prioridade",
    )
    '''status: aberto (true) , fechado (false)'''
    oppened_status = models.BooleanField(
        default=True,
        help_text="aberto ou fechado?",
        verbose_name="status",
    )
    def __str__(self):
        return self.description

class Sample(models.Model):
    description = models.CharField(
        help_text="Descrição de Amostra",
        max_length=80,
        verbose_name="descricao de amostra",
    )
    evalueted_local_sector = models.CharField(
        help_text="Setor Avaliado",
        max_length=80,
        verbose_name="setor avaliado",
    )
    collection_time = models.CharField(
        help_text="Hora da Coleta",
        max_length=80,
        verbose_name="hora da coleta",
    )
    collection_date = models.CharField(
        help_text="Data da Coleta",
        max_length=80,
        verbose_name="data da coleta",
    )

class Parameter(models.Model):
    standard = models.CharField(
        help_text="Norma, Lei, Resolução",
        max_length=200,
        verbose_name="standard",
    )

    description = models.CharField(
        help_text="Parâmetro",
        max_length=200,
        verbose_name="parametro"
    )
    type = models.CharField(
        help_text="Tipos de Parâmetros(físico-químicos, microbiologicos)",
        max_length=80,
        verbose_name="tipos",
    )
    def __str__(self):
        return self.description
