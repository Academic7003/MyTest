from dataclasses import fields
from rest_framework import serializers
from main.models import *

class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'
    
class MaterialSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Xomashyo
        fields = '__all__'