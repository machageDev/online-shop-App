from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=254)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
        CATEGORY_CHOICES = [
      
            ('men','Men'),
            ('women','Women'),
            ('kids','Kids'),
            ('shoes','Shoes'),
            ('accessories','Accessories'),
        ]
        name = models.CharField(max_length=200)
        description = models.TextField(max_length=200)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        category = models.CharField(max_length=11, choices=CATEGORY_CHOICES)
        image = models.ImageField(upload_to='products/')
        color = models.CharField(max_length=200)
        
        def __str__(self):
            return self.name
            
    
    
   