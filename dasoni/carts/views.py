from django.shortcuts import render, redirect
from .models import Cart, Cartitem, Product
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    #product = Product.objects.get(id=product_id)
    #try:
    #    cart = Cart.objects.get(cart_id=_cart_id(request))    
    pass