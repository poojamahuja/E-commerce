from django.db import models
from customer.models import Customer, Address
from store.models import Product


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='order', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, related_name='order_address', on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitem', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return 'OrderItem {}'.format(self.id)


class Coupon(models.Model):
    code = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.code)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return 'Cart {}'.format(self.id)
