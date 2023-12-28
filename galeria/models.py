from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galaxia"),
        ("PLANETA", "Planeta")
    ]
    
    #incluir rodas as colunas desejadas
    nome = models.CharField(max_length=100, null=False, blank=False) #blank significa a mesma coisa que x = ''
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False) 
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    
    #Boa prárica é criar essa função abaixo para devolver as colunas acima
    def __str__(self):
        return self.nome
