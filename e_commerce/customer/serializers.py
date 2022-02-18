from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
