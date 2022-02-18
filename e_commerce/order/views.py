from rest_framework import viewsets
from .serializers import CartSerializer, CartAddSerializer, OrderSerializer, OrderItemSerializer, CouponSerializer
from .models import Cart, Order, OrderItem, Coupon
from store.models import Product
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CartView(generics.ListAPIView):
    # queryset = Cart.objects.all()
    # serializer_class = CartSerializer

    def get(self, request):
        cart_items = Cart.objects.all()

        # customer = []
        # for j in cart_items:
        #     customer.append({
        #         'customer_name': j.customer.username,
        #     })
        items_data = []
        for item in cart_items:
            items_data.append({
                'product_name': item.product.name,
                'product_price': item.product.price,
                'product_quantity': item.product.quantity,
            })
        data = {
            #'customer':customer,
            'items': items_data,
        }

        return Response(status=status.HTTP_200_OK, data=data)


class CartAddView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartAddSerializer


class CartDelView(generics.DestroyAPIView):
    queryset = Cart.objects.all()

    def delete(self, request, pk):
        user = request.user
        cart_item = Cart.objects.filter(customer=user)
        target_product = get_object_or_404(cart_item, pk=pk)
        product = get_object_or_404(Product, id=target_product.product.id)
        product.quantity = product.quantity + target_product.quantity
        product.save()
        target_product.delete()
        return Response(status=status.HTTP_200_OK, data={"detail": "Item deleted from cart"})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
