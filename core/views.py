from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from core.models import Produto

def index(request):#página inicial
    
    produtos = Produto.objects.all()
    
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é top',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):#página de contato
    return render(request, 'contato.html')

def produto(request, pk):#página de produto, traz os dados de cada produto filtrando pelo id=pk
    # prod = Produto.objects.get(id=pk)
    #redireciona para página de erro caso não encontre a página solicitada
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):#apresenta página personalizada de erro (404)
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):#apresenta página personalizada de erro (500)
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

# testando colaboração.
# testando a proteção de branch
