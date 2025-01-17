from django.db import models

#Aqui no models as classes são tabelas no banco de dados, os atributos são as colunas, e os atributos tem suas label (nome, sobrenome por exemplo)
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')
    
    #esta função retorna o nome do objeto de acordo com suas características, geralmente colocamos pra retornar o nome, mas podemos concatenar várias informações do objeto.
    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
