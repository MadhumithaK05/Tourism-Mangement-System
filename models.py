from django.db import models

# Create your models here.
class Customers(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    password=models.CharField(max_length=100)
    conpwd=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.username}({self.password})"
