from unicodedata import name
from main.models import *
from rest_framework.response import Response
from main.api.serilaizers import *
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST', 'GET'])
def create_product(request):
    if request.method == "GET":
        products = ProductModel.objects.all()
        serializer = ProductSerilizer(products, many=True)
        return Response(serializer.data)
    else:
        serializer = ResponseMaterialSerializer(data=request.data)
        
        if serializer.is_valid():
            pr_id = serializer.data['product_id']
            count = serializer.data['product_qty']
            try:
                pr2_id = serializer.data['product_id_']
                count2 = serializer.data['product_qty_']
            except:
                pass
            prod = ProductMaterialsModel.objects.filter(name_id=pr_id)
            warhou = WareHouseModel.objects.filter(material_id__in=[i.material_id for i in prod])
            print([count*float(i.quantity) for i in prod])
            print([i.id for i in prod])

            
            for i in warhou:
                print(i)
            print(warhou)


            
        return Response(request.data)
    



@api_view(['POST'])
def create_material(request):
    serializer = MaterialSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
