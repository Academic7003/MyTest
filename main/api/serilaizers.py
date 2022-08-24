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
        fields = ['name']

class ResponseMaterialSerializer(serializers.Serializer):
    product_qty = serializers.IntegerField()
    product_id = serializers.IntegerField()
    product_qty2 = serializers.IntegerField()
    product_id2 = serializers.IntegerField()

    
    class Meta:
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    material = MaterialSerilizer()
    class Meta:
        model = WareHouseModel
        fields = '__all__'

    def create(self):
     return WareHouseModel(**self.validated_data)

class ResponseSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=255)
    product_qty = serializers.IntegerField()
    product_materials = WarehouseSerializer(many=True)

    class Meta:
        fields = '__all__'





