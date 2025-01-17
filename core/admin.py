from django.contrib import admin
#importando meus modelos
from .models import Produto, Cliente

#mostra os campos do objeto, neste caso da classe Produto (tem colocar todos os campos) e aparentemente substitui o def __str
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

#registrando meus modelos
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)



