"""
URL configuration for vinay_e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from my_store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login/',getLoginForm, name="login_page"),
    path('login-user', loginUser, name='login_user'),
    path('Logout/', logoutUser, name='logout_user'),
    path('', showStore, name='show_store'),
    path('register/', getRegistrationForm, name="registration_page"),
    path('register-user/', registerUser, name="register_user"),
    path('add-to-cart/', addToCart, name="add_to_cart"),
    path('remove-from-cart/<product_id>/', removeFromCart, name="remove_from_cart"),
    path('cart/', getCart, name="show_cart"),
    path('proceed-to-buy/', proceedToBuy, name="proceed_to_buy"),
    path('submit-order/', submitOrder, name="submit_order"),
    path('order-success/',orderSuccess, name="order_success"),
    path('my-orders/', myOrders, name="my_orders")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
