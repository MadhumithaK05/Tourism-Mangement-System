from django.db import models

# Create your models here.
class Customers(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField()
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.username}({self.password})"


class Transaction(models.Model):
    username=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    number_pass=models.IntegerField()
    price=models.IntegerField()
    
    def __str__(self):
        return f"{self.username}({self.price})"