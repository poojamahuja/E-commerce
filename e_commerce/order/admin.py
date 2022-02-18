from django.contrib import admin
from .models import OrderItem, Order, Coupon,Cart

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Cart)
