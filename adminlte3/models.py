from django.db import models

class Area_Especial(models.Model):
    ide_area_especial = models.IntegerField(null=False)
    cod_area_especial = models.IntegerField(null=False)
    nom_area_especial = models.IntegerField(null=False)

    class Meta:
        db_table = 'area_especial'

def __str__(self):
        return self.nom_area_especial  

class Area_Especial_Municipio(models.Model):
    ide_area_especial = models.IntegerField(null=False)
    ide_municipio  = models.IntegerField(null=False)

    class Meta:
        
        db_table = 'area_especial_municipio'

def __str__(self):
        return self.nom_area_especial  
  
class Municipio(models.Model):
    nom_municipio = models.CharField(max_length=20, null=False)
    ide_municipio = models.IntegerField(null=False)
    ide_pais      = models.IntegerField(null=True)    
    lat_municipio = models.CharField(max_length=50, null=True)
    lon_municipio = models.CharField(max_length=50, null=True)
    ind_capital   = models.CharField(max_length=1, null=True)
    alt_municipio = models.CharField(max_length=50, null=True)
    area_municipio = models.CharField(max_length=50, null=True)
    des_status = models.CharField(max_length=1, default='A')
    qtd_populacao = models.IntegerField(max_length=50, null=True)

    class Meta:
        db_table = 'municipio'

def __str__(self):
        return self.nom_municipio

class Cisternas(models.Model):     
    nom_beneficiario = models.CharField(max_length=100, null=False)
    cpf_beneficiario = models.CharField(max_length=11, null=False)
    nis_beneficiario = models.CharField(max_length=12, null=False)
    tip_executor = models.CharField(max_length=20, null=False)
    cod_implementacao = models.IntegerField(null=False)
    nom_comunidade = models.CharField(max_length=50, null=False)
    nom_convenio = models.CharField(max_length=20, null=False)
    tip_situacao = models.CharField(max_length=50, null=False)
    dat_inicio_construcao = models.DateField(null=False)
    dat_fim_construcao = models.DateField(null=False)
    tip_aprovacao = models.CharField(max_length=20, null=False)
    dat_aprovacao = models.DateField(null=False)
    ide_municipio = models.IntegerField(default=0, null=False)

    class Meta:
        managed = False
        db_table = 'cisternas'
        

def __str__(self):
        return self.nom_beneficiario

class Alimentos(models.Model):     
    dat_ano = models.IntegerField(null=False)
    dat_mes = models.IntegerField(null=False)    
    cpf_produtor = models.IntegerField(null=False)    
    ide_municipio = models.IntegerField(null=False)
    ide_alimento = models.IntegerField(null=False)    
    qtd_alimento = models.FloatField(null=False)
    val_alimento = models.FloatField(null=False)
    des_tipo_alimento = models.CharField(max_length=50, null=False)   

    class Meta:
        db_table = 'alimentos'
        
def __str__(self):
        return self.cpf_produtor 

class TipoAlimento(models.Model):     
    des_tipo_alimento = models.CharField(max_length=100, null=False)   

    class Meta:
        db_table = 'tipoalimento'
        
def __str__(self):
        return self.des_tipo_alimento   

class Produtor(models.Model):     
    cpf_produtor = models.IntegerField(null=False)    
    des_produtor = models.CharField(max_length=150, null=False) 

    class Meta:
        db_table = 'produtor'
        
def __str__(self):
        return self.des_produtor 

class Refeicoes(models.Model):     
    ide_municipio = models.IntegerField(null=False)
    dat_ano = models.IntegerField(null=False)
    dat_mes = models.IntegerField(null=False)    
    ide_restaurante = models.IntegerField(null=False)   
    des_faixaetaria = models.CharField(max_length=50, null=False) 
    ide_tipo_refeicao = models.IntegerField(null=False)   

    class Meta:
        db_table = 'refeicoes'

class Restaurante(models.Model):     
    des_restaurante = models.CharField(max_length=100, null=False)   

    class Meta:
        db_table = 'restaurante'
        
def __str__(self):
        return self.des_restaurante 

class EntregasLeite(models.Model):     
     ano_entrega = models.IntegerField(null=False)
     mes_entregs = models.IntegerField(null=False)
     ide_municipio = models.IntegerField(null=False)
     ide_laticinio = models.IntegerField(null=False)
     ide_entidade = models.IntegerField(null=False)
     ide_tipo_leite = models.IntegerField(null=False)
     qtd_entrega = models.FloatField(null=False)
     val_entrega = models.FloatField(null=False)
     des_status = models.CharField(max_length=1, null=False, default = 'A') 

     class Meta:
        db_table = 'entregas_leite'
        
def __str__(self):
        return self.ide_laticinio 
