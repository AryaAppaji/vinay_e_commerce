from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages for displaying messages

from .forms import LoginForm
from .models import Product

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:  # and user.id != 1:
                login(request, user)
                return redirect('products_page')  # redirect to the named URL of the products page
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials or unauthorized user.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')  # Optional: Display a logout message
    return redirect('login')

@login_required
# Assuming you have a separate view for the products page:
def products_page(request):
    product_list = Product.objects.all()
    return render(request, 'products_page.html', {"products": product_list})
