from django.shortcuts import redirect, render
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import Cart
from django.contrib.auth.decorators import login_required


def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantite :
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems :
        total_price = total_price + item.product.prix * item.product_qty
    
    context = {'cartitems':cartitems, 'total_price':total_price}
    return render(request, "store/checkout.html", context)   