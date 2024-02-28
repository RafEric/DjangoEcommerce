from django.shortcuts import redirect,render 
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:4]  # Récupérer les 5 derniers produits
    return render(request, "store/index.html", {'latest_products': latest_products} )
"""def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    categories = Category.objects.filter(status=0)  # Récupérer les catégories avec le statut 0
    context = {
        'latest_products': latest_products,
        'categories': categories,  # Ajouter les catégories au contexte
    }
    return render(request, "store/index.html", context)"""

def collections(request):
    category = Category.objects.filter(status=0)
    context =  {'category':category}
    return render(request, "store/collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products =  Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products' : products, 'category': category }
        return render(request, "store/products/index.html", context)
    else:
        messages.warning(request, "no such category no found")
        return redirect('collections')
    
def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.error(request, "No such product found")     
            return redirect('collections')
    
    else: 
        messages.error(request, "No such category found")     
        return redirect('collections')
    
    return render(request, "store/products/view.html", context)

def product_list(request):
    latest_products = Product.objects.all().order_by('-added_at')[:5]  # Récupérer les 5 derniers produits
    return render(request, 'store/index.html', )

