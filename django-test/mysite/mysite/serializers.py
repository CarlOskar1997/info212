from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'carmodel'] 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        name = Employee
        fields = ['Employee_id', 'name', 'age']