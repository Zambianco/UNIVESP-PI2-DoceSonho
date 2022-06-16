from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,1000)]
class AdicionarCarrinho(forms.Form):
    quantidade = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False,widget=forms.HiddenInput)
