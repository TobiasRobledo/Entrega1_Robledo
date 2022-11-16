from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return f"Name: {self.name} - Description: {self.description} - Price: {self.price}"

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
        
    def __str__(self):
        return f"Name: {self.name} - Description: {self.description}"


class Order(models.Model):
    number = models.IntegerField()
    total = models.DecimalField(max_digits=9, decimal_places=2)
        
    def __str__(self):
        return f"Number: {self.number} - Total: {self.total}"
