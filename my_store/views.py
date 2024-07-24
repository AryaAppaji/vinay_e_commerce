from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Product, BillingDetails

def getLoginForm(request):
    return render(request, "login_page.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.id != 1:  # Check if user ID is not 1
                login(request, user)
                return redirect("show_store")
        return render(request, "login_page.html", {
            "message": "Invalid Credentials"
        })

@login_required
def logoutUser(request):
    logout(request)
    return redirect("login_page")

def showStore(request):
    user_logged_in = request.user.is_authenticated
    products = Product.objects.all()
    cart_items = request.session.get("product_list",[])
    return render(request, 'show_store.html', {
        "products": products,
        "login_status": user_logged_in,
        "cart_count": len(cart_items)
    })

def getRegistrationForm(request):
    return render(request, "registration.html")

def registerUser(request):
    name = request.POST.get("name")
    user_name = request.POST.get("user_name")
    password = request.POST.get("password")
    mobile_number  = request.POST.get("mobile_number")
    address = request.POST.get("address")

    user = User.objects.create(username = user_name, password = make_password(password))

    user_details = BillingDetails.objects.create(user_id = user, name=name,contact_no=mobile_number, address=address)

    if user and user_details:
        return redirect("login_page")
    
def addToCart(request):
    item = request.POST.get("product_id")
    if item not in request.session.get("product_list", []):
        cart_items = request.session.get("product_list", [])
        cart_items.append(item)
        request.session["product_list"] = cart_items
    return redirect("show_store")

def removeFromCart(request):
    item = request.POST.get("product_id")
    cart_items = request.session.get("product_list", [])
    if(item in cart_items):
        cart_items.remove(item)
        request.session["product_list"] = cart_items
    return redirect("show_cart")

def getCart(request):
    user_logged_in = request.user.is_authenticated
    items = request.session.get("product_list")
    products = Product.objects.filter(id__in=items)

    return render(request, 'cart.html', {
        "products": products,
        "login_status": user_logged_in,
        "cart_count": len(items)
    })
