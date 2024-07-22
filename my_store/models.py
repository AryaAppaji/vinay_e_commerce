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
    user_id = models.OneToOneField(User, models.CASCADE)
    name = models.CharField(max_length=50)
    address  = models.TextField()
    contact_no = models.CharField(max_length=10)
    class Meta:
        db_table = 'billing_details'