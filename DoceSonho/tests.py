from django.test import TestCase
from django.urls import reverse
import json

from Portfolio.models import Produtos
from Classificacao.models import Categoria


# Create your tests here.

class ProdutosModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Categoria.objects.create(nomeCategoria='bolos')
        Produtos.objects.create(titulo='Bolo de chocolate', descricao='delicioso bolo de chocolate', categoria_id=1)

    def test_str_is_titulo(self):
        produto = Produtos.objects.get(ID=1)
        expected_object_name = produto.titulo
        self.assertEquals(expected_object_name, str(produto))


    def test_titulo_max_lenth(self):
        produto = Produtos.objects.get(ID=1)
        max_length = produto._meta.get_field('titulo').max_length
        self.assertEquals(max_length, 200)

class ProdutosViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests

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

    def test_list_produtos(self):
        response = self.client.get('/listProdutos/')
        self.assertEqual(response.status_code, 200)
        produtoList = json.loads(response.content)
        self.assertEqual(len(produtoList),20)

    def test_list_categorias(self):
        response = self.client.get('/listCategoria/')
        self.assertEqual(response.status_code, 200)
        categoriaList = json.loads(response.content)
        self.assertEqual(len(categoriaList),2)