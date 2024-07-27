from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField(upload_to="images/")
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    class Meta:
        db_table = "products"
    
    def __str__(self) -> str:
        return f"{self.name} ({self.description})"


class BillingDetails(models.Model):
    user_id = models.OneToOneField(User, models.CASCADE, related_name="details")
    name = models.CharField(max_length=50)
    address  = models.TextField()
    contact_no = models.CharField(max_length=10)
    class Meta:
        db_table = 'billing_details'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    customer_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=10)
    customer_address = models.TextField()
    date = models.DateField(auto_now_add=True)
    total_amount = models.FloatField()

    class Meta:
        db_table = 'orders'  

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=50)
    description = models.TextField()
    image_path = models.CharField(max_length=255)
    price = models.FloatField()
    qty = models.IntegerField()

    class Meta:
        db_table = 'order_items'