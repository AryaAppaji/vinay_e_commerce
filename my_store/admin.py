from django.contrib import admin
from .models import Product, Order, OrderItem

# Register your models here.

admin.site.site_header = "Vinay Zone Admin Portal"
admin.site.index_title = "Vinay Zone Admin Portal"

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
