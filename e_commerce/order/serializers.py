import decimal
from rest_framework import serializers
from .models import Order, OrderItem, Cart, Coupon
from store.serializers import ProductSerializer
from customer.serializers import CustomerSerializer
from customer.models import Customer
from store.models import Product
from django.shortcuts import get_object_or_404


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'address', 'created']


class OrderItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField('count_total')

    class Meta:
        model = OrderItem
        fields = ['order', 'coupon', 'product', 'quantity', 'total']

    def count_total(self, order):
        coupon = order.coupon  # Coupon name
        # print(coupon)
        discount = coupon.amount  # Discount on coupon
        product = order.product  # Product name
        # print(product)
        product_price = product.price  # Product price
        product_quantity = order.quantity  # Product Quantity
        total_amount = decimal.Decimal(product_quantity * product_price) - discount
        order.total = decimal.Decimal(total_amount)
        # order.save()
        return order.total


class CartSerializer(serializers.ModelSerializer):
    #product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ['customer', 'product', 'quantity', 'price']


class CartAddSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ('quantity', 'product_id')
        extra_kwargs = {
            'quantity': {'required': True},
            'product_id': {'required': True},
        }

    def create(self, validated_data):
        user = Customer.objects.get(id=self.context['request'].user.id)
        product = get_object_or_404(Product, id=validated_data['product_id'])
        if product.quantity == 0:
            raise serializers.ValidationError(
                {'not available': 'the product is out of stock.'})

        quantity = validated_data['quantity']
        price = product.price * quantity
        print(price)

        cart_item = Cart.objects.create(
            customer=user,
            product=product,
            quantity=validated_data['quantity'],
            price=price
        )
        cart_item.save()
        product.quantity = product.quantity - cart_item.quantity
        product.save()
        return cart_item


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['code', 'amount']
