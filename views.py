from django.shortcuts import render,HttpResponse,HttpResponseRedirect
# Create your views here.
from django.contrib.auth.hashers import make_password,check_password
from .models import Product
from .models import Category,Customer,Order
from django.contrib.auth.decorators import login_required
#-----------------------------------------------------Password Hashing-----------------
#print(make_password('1234'))
#print(check_password('1234','pbkdf2_sha256$216000$5LNTXule2xKk$rmNMZLj3MiLXKsyFq1L2T3WRWu7TrljmgU6NK+ENSmA='))
#---------------------------------------------------------------------------------------
def index(request):
    cart=request.session.get('cart')       #..............donot remove this line...............
    if not cart:
        request.session['cart']={}
    products=Product.objects.all()
    category=Category.objects.all()
    return render(request,'Store/index.html',{'products':products,'category':category})

def addcart(request):
    if request.method=="POST":
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        print(remove)
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        products=Product.objects.all()
        category=Category.objects.all()
        return render(request,'Store/index.html',{'products':products,'category':category})
def category_function(request):
    cat=request.GET['category']
    catg=Product.objects.filter(category=cat)
    category=Category.objects.all()
    return render(request,'Store/index.html',{'products':catg,'category':category})


def All_product_function(request):
    prod=Product.objects.all()
    category=Category.objects.all()
    #print(request.session['email'])
    #print(request.session['customer_id'])
    return render(request,'Store/index.html',{'products':prod,'category':category})

def signuppage(request):
    return render(request,'Store/signup.html')

def customersignup(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        phone=request.POST['phoneno']
        email=request.POST['email']
        password=request.POST['password']
        msg=""
        msg1=""
        msg3=""
        msg4=""
        msg5=""
        bool=phone.isdigit()
        user=Customer.objects.filter(email=email)
        if len(fname) <6:
            msg="First Name must be 6 character Long"
            return render(request,'Store/signup.html',{'msg':msg,'fname':fname,'lname':lname,'phone':phone,'email':email,'password':password})
        elif len(lname) <4:
            msg1="Last Name must be 4 character Long"
            return render(request,'Store/signup.html',{'msg1':msg1,'fname':fname,'phone':phone,'email':email,'password':password,'lname':lname})
        elif len(phone) <10:
            msg3="Phone No must be 10 character Long"
            return render(request,'Store/signup.html',{'msg3':msg3,'fname':fname,'phone':phone,'email':email,'password':password,'lname':lname})
        elif bool==False:
            msg3="PhoneNo must be Numeric Value"
            return render(request,'Store/signup.html',{'msg3':msg3,'fname':fname,'phone':phone,'email':email,'password':password,'lname':lname})
        elif len(email) <10:
            msg4="Email No must be 10 character Long"
            return render(request,'Store/signup.html',{'msg4':msg4,'fname':fname,'phone':phone,'email':email,'password':password,'lname':lname})
        elif len(password) <4:
            msg5="Password Must be 4 character Long"
            return render(request,'Store/signup.html',{'msg5':msg5,'fname':fname,'email':email,'password':password,'phone':phone,'lname':lname})
        elif user:
            msg4="Email Already Exists"
            return render(request,'Store/signup.html',{'msg4':msg4,'fname':fname,'phone':phone,'email':email,'password':password,'lname':lname})
        else:
            msg2="ACCOUNT CREATED SUCCESSFULLY"
            customer=Customer(first_name=fname,last_name=lname,phone=phone,email=email,password=make_password(password))
            customer.save()
            return render(request,'Store/signup.html',{'msg2':msg2})

#-----------------------------------------------------------LOGIN------------------------------------------------------
def customerLoginpage(request):
    return render(request,'Store/login.html')

def customerlogin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=Customer.objects.get(email=email)
        bool=check_password(password,user.password)
        if user and bool==True:
            request.session['customer']=user.id
            request.session['email']=user.email
            return HttpResponseRedirect('/Store/home')
        else:
            error="Invalid Email or Password"
            return render(request,'Store/login.html',{'msg':error})

def customerLogout(request):
    request.session.clear()
    return HttpResponseRedirect("/Store/Login/")

def customercart(request):
    if 'cart' in request.session:
        ids=list(request.session.get('cart').keys())
        products=Product.objects.filter(id__in=ids)
        return render(request,'Store/cart.html',{'ids':ids,'products':products})
    else:
        return HttpResponseRedirect('/Store/Login/')

def customercheckout(request):
    if request.method=="POST":
        address=request.POST['address']
        phone=request.POST['phone']
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.objects.filter(id__in=list(cart.keys()))
        for product in products:
            order=Order(customer=Customer(id=customer),product=product, price=product.price, quantity=cart.get(str(product.id)), address=address, phone=phone)
            order.save()
            request.session['cart']={}
        print(address,phone,customer,cart,products)
        return HttpResponseRedirect('Store/cart/')

def customerorder(request):
    customer=request.session.get('customer')
    order=Order.objects.filter(customer=customer).order_by('-date')
    print(order)
    return render(request,'Store/order.html',{'order':order})
