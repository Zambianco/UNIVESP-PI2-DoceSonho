from django.shortcuts import render, get_object_or_404, redirect
from Portfolio.models import Produtos
from .cart import Cart
from .forms import AdicionarCarrinho


from django.http import JsonResponse


def cart_add(request, IDproduto, qtd):
    """Adiciona itens ao carrinho"""
    cart = Cart(request)
    product = get_object_or_404(Produtos, ID=IDproduto)
    #form = AdicionarCarrinho(request.POST)
    #if form.is_valid():
        #cd = form.cleaned_data
    cart.add(product=IDproduto, quantity=qtd)
    return redirect('cart:cart_detail')


def cart_cookie(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    return cart


def cart_remove(request, IDproduto):
    """Remove itens do carrinho"""
    cart = Cart(request)
    produtct = get_object_or_404(Produtos, ID=IDproduto)
    cart.remove(IDproduto)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = list(Cart(request))[1]
    return JsonResponse(cart, safe=False) 
