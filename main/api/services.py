from main.models import WareHouseModel
from math import ceil


def needs_dict_returner(products, product_need):
    needs_list = [ceil(product_need*float(i.quantity)) for i in products]
    needs_id = [i.material_id for i in products]
    needs_dict = dict(zip(needs_id, needs_list))
    return needs_dict


def fix_needs(list, needs_dict):
        for k,v in needs_dict.items():
            if v==0:
                continue
            else:
                create_warehouse_serializer(list, WareHouseModel(material_id=k, remainder=v))


def create_warehouse_serializer(list, obj):
    list.append(obj)

