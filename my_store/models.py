from django.db import models

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