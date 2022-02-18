from django.db import models
from customer.models import Customer
from order.models import Order, OrderItem


# Create your models here.
class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='invoice', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Invoice {}'.format(self.invoice_id)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='invoice_item', on_delete=models.CASCADE)
    order_item = models.ForeignKey(OrderItem, related_name='order_item', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return 'Invoice Item {}'.format(self.id)


class Payment(models.Model):
    order = models.ForeignKey(Order, related_name='payment_item', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='payment', on_delete=models.CASCADE)
    type = models.CharField(max_length=10)

    def __str__(self):
        return 'Payment {}'.format(self.id)
