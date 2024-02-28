from django.urls import path
from . import views
from store.controller import authview, cart, viewlist,checkout


urlpatterns = [
    path('', views.home , name="home"),
    path('collections', views.collections,name="collections"),
    path('collections/<str:slug>',views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/s<str:prod_slug>', views.productview, name="productview"),
    path('register/', authview.register, name="register"),
    path('login/',authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage,name="logout"),
    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('viewlist', viewlist.index, name="viewlist"),
    path('add-to-viewlist', viewlist.addtoviewlist, name="addtoviewlist"),
    path('checkout', checkout.index, name="checkout"),
]
