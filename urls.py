from Store import views
from django.conf.urls import url

urlpatterns = [
  url('home',views.index),
  url('Catg',views.category_function),
  url('AllProd',views.All_product_function),
  url('Signup',views.signuppage),
  url('signup1',views.customersignup),
  url('Login',views.customerLoginpage),
  url('login',views.customerlogin),
  url('logout',views.customerLogout),
  url('AddCart',views.addcart),
  url('cart',views.customercart),
  url('checkout',views.customercheckout),
  url('place-order',views.customerorder),
]
