from dataclasses import fields
from rest_framework import serializers
from main.models import *

class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
    
class MaterialSerilizer(serializers.ModelSerializer):

    class Meta:
        model = MaterialModel
        fields = '__all__'

class ResponseMaterialSerializer(serializers.Serializer):
    product_qty = serializers.IntegerField()
    product_id = serializers.IntegerField()
    product_qty_ = serializers.IntegerField()
    product_id_ = serializers.IntegerField()
    
    class Meta:

        fields = '__all__'