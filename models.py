from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='products/')
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=500)
    def __str__(self):
        return self.first_name
import datetime
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE,)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=100,blank=True)
    price=models.IntegerField(blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
