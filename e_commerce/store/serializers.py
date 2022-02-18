from rest_framework import serializers
from .models import Store, Employee, Product


class ProductSerializer(serializers.ModelSerializer):
   class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'description', 'price']
