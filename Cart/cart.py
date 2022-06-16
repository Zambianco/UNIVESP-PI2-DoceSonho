from django.conf import settings
from Portfolio.models import Produtos
class Cart(object):
    def __init__(self, request):
        """Inicialização do carrinho"""
        self.session=request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart

    def add(self,product,quantity=1,override_quantity=False):
        """Adiciona itens ao carrinho"""
        product_id = str(product)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0}
        if override_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, Produtos):
        """Remove itens ao carrinho"""
        product_id = str(Produtos)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        product = Produtos.objects.filter(ID__in=product_ids)
        return iter(self.__dict__.items())
        cart = self.cart.copy()
       
        
