from django.db import models

from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%s')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150, null= False, blank=False)
    marque = models.CharField(max_length=150, null= False, blank=False)
    image = models.ImageField( upload_to = get_file_path, null=True, blank = True)
    description = models.TextField(max_length=500,null=False, blank=False)
    status =  models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending =  models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500,null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.marque
    
class Product(models.Model):
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null= False, blank=False)
    marque = models.CharField(max_length=150, null= False, blank=False)
    produit_image = models.ImageField(upload_to = get_file_path, null=True, blank = True)
    petite_description = models.CharField(max_length=250,null=False, blank=False)
    quantite = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)
    prix = models.FloatField(null=False, blank=False)
    status =  models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending =  models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    tag =  models.CharField(max_length=150, null= False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500,null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.marque
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Viewlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)