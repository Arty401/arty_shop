from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import FormView, TemplateView

from product.models import Laptop
from . import forms
from .cart import Cart


@login_required()
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@login_required()
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


@login_required()
def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Laptop, id=id)
    cart.remove(product)
    return redirect('detail')


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('detail')
