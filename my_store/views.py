from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product

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
    return render(request, 'show_store.html', {
        "products": products,
        "login_status": user_logged_in
    })