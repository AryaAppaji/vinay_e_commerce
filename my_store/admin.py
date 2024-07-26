from django.contrib import admin
from .models import Product,Order,OrderItem
# Register your models here.

admin.site.site_header = "Vinay Zone Admin Portal"
admin.site.index_title = "Vinay Zone Admin Portal"
admin.site.register([Product, Order, OrderItem])