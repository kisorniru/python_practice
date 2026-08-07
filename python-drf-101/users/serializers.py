from rest_framework import serializers
from .models import User, Address

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        feilds = ['id', 'email', 'first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        feilds = ['id', 'street', 'city', 'country', 'division', 'postal_code', 'additional_info', 'is_primary']