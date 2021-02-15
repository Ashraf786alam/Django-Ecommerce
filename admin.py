from django.contrib import admin
from .models import Product,Category,Customer,Order

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCustomer(admin.ModelAdmin):
        list_display=['first_name','last_name','phone','email','password']

class AdminOrder(admin.ModelAdmin):
        list_display=['product','customer','quantity','price','date']

admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)
