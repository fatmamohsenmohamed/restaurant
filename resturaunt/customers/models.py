from django.db import models

# Create your models here.
# Model: Customer
# - name (string)
# - email (optional)
# - phone (string)
# Relations:
# - One-to-Many: Customer → Orders
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} , {self.email} , {self.phone}"


