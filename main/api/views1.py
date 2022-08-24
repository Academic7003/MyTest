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
            pr_id2 = serializer.data['product_id2']
            count2 = serializer.data['product_qty2']

            # berilgan mahsulotni bittasi u.n kerak hom ashyoni chiqarib. bizga k.k miqdorga kopaytiryapman
            prod = ProductMaterialsModel.objects.filter(name_id=pr_id)
            prod2 = ProductMaterialsModel.objects.filter(name_id=pr_id2)

            # ombordan bizga k.k mahsulotlarni partiyasidan qatiynazar chaqiryapman
            warhou = WareHouseModel.objects.filter(material_id__in=[i.material_id for i in prod])
            t = WareHouseModel.objects.filter(material_id__in=[i.material_id for i in prod])
            warhou2 = WareHouseModel.objects.filter(material_id__in=[i.material_id for i in prod2])


            needs_list = [count*float(i.quantity) for i in prod]
            needs_id = [i.material_id for i in prod]
            # print(needs_list)
            # print(needs_id)
            # 2
            needs_list2 = [count*float(i.quantity) for i in prod2]
            needs_id2 = [i.material_id for i in prod2]
            changed = []
            materchan = []
            needs_dict = dict(zip(needs_id, needs_list))
            print(needs_dict)

            

            for i in warhou:
                for k,v in needs_dict.items():
                    if v==0:
                        continue
                    if i.material_id==k:
                        z = i.remainder -v
                        changed.append(i.id)
                        if z<0:
                            needs_dict[k] = v- i.remainder
                        elif z==0:
                            needs_dict[k] = 0
                            changed.append(k)
                        elif z>0:
                            i.remainder=v
                            
                            needs_dict[k] = 0
                            qwe=t.filter(material_id=i.material_id, id=i.id).first()
                            qwe.remainder= qwe.remainder-z
            for i in warhou.filter(id__in=changed):
                for k,v in needs_dict.items():
                    if v==0:
                        continue
                    if i.material_id==k:
                        z = i.remainder -v
                        changed.append(i.id)
                        if z<0:
                            needs_dict[k] = v- i.remainder
                        elif z==0:
                            needs_dict[k] = 0
                            changed.append(k)
                        elif z>0:
                            i.remainder=v
                            
                            needs_dict[k] = 0
                            qwe=t.filter(material_id=i.material_id, id=i.id).first()
                            qwe.remainder= qwe.remainder-z
            in_base = WarehouseSerializer(t, many=True)
            in_base2 =WarehouseSerializer(warhou, many=True)

            print(needs_dict)
            print(changed)

            for i in changed:
                try:
                    needs_dict.pop(i)
                except:
                    pass
            # print(needs_dict)


            # print(needs_list2)
            # print(needs_id2)
            # print(dict(zip(needs_id2, needs_list2)))

            # in_base = [0 for i in needs_id]
            # in_base2 = [0 for i in needs_id2]

            # print(in_base.data)
            # print(11111111111111111111111111111111111111111)
            # print(in_base2.data)
            # print(t==warhou)
            # for i in warhou:
            #     for j in needs_id:
            #         if i.material_id == j:
            #             in_base[str(needs_id.index(j))]=i.remainder
            # print(in_base)

            # for i in warhou2:
            #     for j in needs_id2:
            #         if i.material_id == j:
            #             in_base2[needs_id2.index(j)]+=i.remainder
            # print(in_base2)
            # data = {}
            # for i in warhou:

            
        return Response(in_base2.data)
    



@api_view(['POST'])
def create_material(request):
    serializer = MaterialSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
