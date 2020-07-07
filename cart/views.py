from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from product.models import Laptop
from . import forms
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Laptop, id=id)
    form = forms.CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('detail')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Laptop, id=id)
    cart.remove(product)
    return redirect('detail')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('detail')
