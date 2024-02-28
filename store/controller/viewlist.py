from django.shortcuts import redirect, render
from django.contrib import messages
from django.http.response import JsonResponse
from store.models import  Viewlist
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def index(request):
    viewlist = Viewlist.objects.filter(user=request.user)
    context = {'viewlist':viewlist}
    return render(request, 'store/viewlist.html', context)

def addtoviewlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Viewlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':'la produit est dans la viewlist'})
                else:
                    Viewlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "aucun produit n'a été trouver"})
            else:
                return JsonResponse({'status':"aucun produit trouver "})
            
        else:
            return JsonResponse({'status':"Login pour continuer"})
        
    return redirect('/')
