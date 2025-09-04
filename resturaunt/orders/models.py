from django.db import models
from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)  # for quick guest orders

    def __str__(self):
        if self.customer:
            return f"Order {self.id} - {self.customer.name}"
        return f"Order {self.id} - {self.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=100)
    item_quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.item_name} x {self.item_quantity}"
