from django.shortcuts import render

from Classificacao.models import Categoria
from .models import Bolo, Doce, Quitute
from django.http import JsonResponse

def listQuitute(request):
    categoria = request.GET['category']

    data = []
    if categoria:
        data = list(Quitute.objects.filter(categoria__id__in=categoria.split(',')).values())
    else:
        data = list(Quitute.objects.values())
    return JsonResponse(data, safe=False)

def listBolo(request):
    data = list(Bolo.objects.values())
    return JsonResponse(data, safe=False)

def listDoce(request):
    data = list(Doce.objects.values())
    return JsonResponse(data, safe=False)

def listCategoria(request):
    data = list(Categoria.objects.values())
    return JsonResponse(data, safe=False)

def bolo_show(request):
    bolos = Bolo.objects.all()
    context = {'bolos': bolos}
    return render(request, 'bolos.html', context)
