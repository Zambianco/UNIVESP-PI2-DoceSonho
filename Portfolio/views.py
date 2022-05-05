from django.shortcuts import render

from Classificacao.models import Categoria
from .models import Produtos
from django.http import JsonResponse

def listQuitute(request):
    categoria = request.GET['category']

    data = []
    if categoria:
        data = list(Quitute.objects.filter(categoria__id__in=categoria.split(',')).values())
    else:
        data = list(Quitute.objects.values())
    return JsonResponse(data, safe=False)

def listProdutos(request):
    data = list(Produtos.objects.values())
    return JsonResponse(data, safe=False)

def listCategoria(request):
    data = list(Categoria.objects.values())
    return JsonResponse(data, safe=False)
