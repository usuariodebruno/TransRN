from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    # Pretendendo usar: first_name, last_name, email
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    cpf = models.CharField(max_length=14, unique=True)
    matricula = models.IntegerField(blank=False, null=False) # Campo obrigatório
    telefone = models.IntegerField(blank=False, null=False) 
    data_nascimento = models.DateField (blank=False, null=False )
    data_admissao = models.DateField (blank=True, null=True ) #  data_evento=date(2024, 10, 20)
    habilitacao = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='images/funcionario/', null=True, blank=True)
    pasep = models.IntegerField(blank=True, null=True) # Não obrigatório  
    observacoes = models.CharField(max_length=5000, blank=True, null=True)   
    # Pode-se incluir: Lotação & Setor 

    def __str__(self):
        return f'{self.user.first_name}'
    
class Habilitacao (models.Model):    
    habilitacao_documento = models.ImageField(upload_to='images/habilitacao/', null=True, blank=True)
    habilitacao_numero = models.IntegerField(blank=False, null=False) # Campo obrigatório
    habilitacao_validade = models.DateField (blank=True, null=True ) #  data_evento=date(2024, 10, 20)
    habilitacao_categoria = models.CharField(max_length=2, unique=True, choices = [
        ('A', 'A'),
        ('AB', 'AB'),
        ('AC', 'AC'),
        ('AD', 'AD'),
        ('AE', 'AE'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),        
        ('E', 'E'),
    ])

    def __str__(self):
        return f'{self.habilitacao_categoria}'
    
class Bairro(models.Model):
    nome = models.CharField(max_length= 200, unique=True) # Padroniza entrada 
    zona = models.CharField(max_length=2, choices=[
        ('ZN', 'Zona Norte'),
        ('ZS','Zona Sul'),
        ('ZL', 'Zona Leste'),
        ('ZO', 'Zona Oeste'),
    ])

    def __str__(self):
        return f'Nome: {self.nome}'
  
class Motorista(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=False)
    habilitacao = models.ForeignKey(Habilitacao, on_delete=models.CASCADE, null=False)    

    def __str__(self):
        return f'Nome: {self.funcionario.user.first_name} (Habilitação: {self.habilitacao})'

class Endereco(models.Model):
    endereco_residencial = models.CharField (max_length=500, blank=False, null=False)
    numero = models.CharField(max_length=10,) 
    cep = models.IntegerField(blank=True, null=True)     
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, null=False, blank=False,)   

    def __str__(self):
        return f'Endereço: {self.endereco_residencial}, Bairro: {self.bairro}'
    
""" 
class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique=True, blank=False, null=False) # Campo obrigatório
    renavam = models.IntegerField(max_length=11, unique=True, blank=False, null=False) # Campo obrigatório
    modelo = models.CharField(max_length=100,) 
    marca =  models.CharField(max_length=100,)# Ford, Toyota
    chassi = models.CharField(max_length=100,)
    observacoes = models.CharField(max_length=5000, blank=True, null=True,)
    motorista_responsavel = models.ForeignKey(Motorista, null=True)

    def __str__(self):
        return f'Nome: {self.placa} (Renavam: {self.renavam})'

class VeiculoLocado(models.Model):
    veiculo = models.ForeignKey(Veiculo, null=False, blank=False)
    nome_locadora = models.CharField(max_length=100, unique=True, blank=False, null=False) # Campo obrigatório
    data_contratacao = models.DateField (blank=False, null=False,) 

    def __str__(self):
        return f'Placa: {self.veiculo.placa} (Locadora: {self.nome_locadora})'

class VeiculoPropio(models.Model):
    veiculo = models.ForeignKey(Veiculo, null=False, blank=False)
    data_aquisicao = models.DateField (blank=False, null=False,) # Data em que o carro foi adquirido.

    def __str__(self):
        return f'Placa: {self.veiculo.placa}'    

class Documento(models.Model):
    documento = models.ImageField(upload_to='images/documento/', null=False, blank=False) # Campo obrigatório
    tipo_documento = models.CharField(max_length=3, choices=[
        ('TR', 'Termo de Responsabilidade'),
        ('CL', 'Check List'),
        ('TE', 'Termo de Entrega'),
        ('OS', 'Ordem de Serviço'),
        ('LIC', 'Licenciamento do Veículo')
        ('CON', 'Contrato')
        ('MUL', 'Multas')
        ('OUT', 'Outros')
    ])
    observacoes = models.CharField(max_length=5000, blank=True, null=True,)
    veiculo_documento = models.ForeignKey(Veiculo, blank=False, null=False,)

    def __str__(self):
        return f'{self.get_tipo_documento_display()}'

class Multas(models.Model):
    local 
    data_hora 
    infracao_descricao = models.CharField(max_length=5000, blank=False, null=False,),
    numero_auto = models.IntegerField(max_length=50, blank=False, null=False,)  
    esfera = models.CharField(max_length=1, choices=[
        ('F', 'Federal'),
        ('E', 'Estadual'),
        ('M', 'Municipal'),
    ],),
    documento = models.ForeignKey(Documento, null=False, blank=False,)
"""