from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True,max_length=254)
    password = models.CharField(max_length=200)
    user = models.ForeignKey=models.CASCADE
    
    def __str__(self):
        return self.email
    