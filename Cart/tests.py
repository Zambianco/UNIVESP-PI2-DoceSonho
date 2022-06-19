from django.test import TestCase
from django.urls import reverse
import json
import uuid
from django.contrib.messages import get_messages

from Portfolio.models import Produtos
from Classificacao.models import Categoria
from Cart.cart import Cart

# Create your tests here.
class CartViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Categoria.objects.create(nomeCategoria='bolos')
        Categoria.objects.create(nomeCategoria='doces')

        number_produtos = 10

        for produto_id in range(number_produtos):
                Produtos.objects.create(
                titulo=f'Bolo {produto_id}',
                descricao=f'Bolo {produto_id}',
                categoria_id=1
        )

        for produto_id in range(number_produtos):
            Produtos.objects.create(
                titulo=f'Doce {produto_id}',
                descricao=f'Doce {produto_id}',
                categoria_id=2
        )

    def test_add_produto(self):
        response = self.client.post(reverse('cart:cart_add', kwargs={'IDproduto':2,'qtd':3,}),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('cart:cart_detail'))

    def test_add_produto_sum_qnt(self):
        response = self.client.post(reverse('cart:cart_add', kwargs={'IDproduto':2,'qtd':3,}),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('cart:cart_detail'))
        response = self.client.post(reverse('cart:cart_add', kwargs={'IDproduto':2,'qtd':5,}),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('cart:cart_detail'))
        dic = json.loads(response.content)
        self.assertEqual(dic[1]['2']['quantity'], 5+3)
        
    def test_cart_detail(self):
        response = self.client.post(reverse('cart:cart_add', kwargs={'IDproduto':2,'qtd':3,}),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('cart:cart_detail'))
        response = self.client.post(reverse('cart:cart_add', kwargs={'IDproduto':14,'qtd':2,}),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('cart:cart_detail'))
        dic = json.loads(response.content)
        self.assertEqual(len(dic[1]),2)
        
    def test_remove_produto(self):
        response = self.client.post(reverse('cart:cart_add', kwargs={'IDproduto':2,'qtd':3,}),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('cart:cart_detail'))
        dic = json.loads(response.content)
        self.assertEqual(len(dic[1]),1)
        response = self.client.post(reverse('cart:cart_remove', kwargs={'IDproduto':2,}),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('cart:cart_detail'))
        dic = json.loads(response.content)
        self.assertEqual(len(dic[1]),0)

    def test_add_invalid_produto(self):
        response = self.client.post(reverse('cart:cart_add', kwargs={'IDproduto':25,'qtd':3,}),follow=True)
        self.assertEqual(response.status_code, 404)

    def test_remove_invalid_produto(self):
        response = self.client.post(reverse('cart:cart_remove', kwargs={'IDproduto':22,}),follow=True)
        self.assertEqual(response.status_code, 404)

    def test_remove_non_cart_produto(self):
        response = self.client.post(reverse('cart:cart_remove', kwargs={'IDproduto':2,}),follow=True)
        self.assertEqual(response.status_code, 404)
        

