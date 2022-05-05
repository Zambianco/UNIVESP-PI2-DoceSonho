from django.urls import path
from . import views

app_name = 'Cart'

urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:IDproduto>qtd<int:qtd>/', views.cart_add, name='cart_add'),
    path('remove/<int:IDproduto>/', views.cart_remove, name='cart_remove'),
    ]
