from django.db import models
from django.contrib.auth.models import User
CATEGORIES = (
    ('stationary' , 'stationary'),
    ('electronics' , 'electronics'),
    ('food' , 'food'),
    )
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20 , choices=CATEGORIES , null=True)
    quantity = models.PositiveIntegerField(null=True)
    def __str__(self):
        return f"{self.name} - {self.quantity}"
    class Meta:
        verbose_name_plural = 'Product'
class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , null=True)
    staff = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.product} ordered by {self.staff.username}"
    class Meta:
        verbose_name_plural = 'Order'