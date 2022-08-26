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


def add_needs_return_list(serial_list, warhou, not_free, needs_dict):
            for i in warhou:
                if i.id in not_free:
                    continue
                for k,v in needs_dict.items():
                    if v==0:
                        continue
                    if i.material_id == k:
                        z = i.remainder - v
                        if z < 0:
                            needs_dict[k] = v- i.remainder
                            create_warehouse_serializer(serial_list, i)

                        elif z == 0:
                            needs_dict[k] = 0
                            create_warehouse_serializer(serial_list, i)
                            not_free.append(i.id)

                        elif z > 0:
                            i.remainder=i.remainder-v
                            create_warehouse_serializer(serial_list, WareHouseModel(part_id=i.part_id, material_id=i.material.id, remainder=v, price=i.price))
                            needs_dict[k] = 0
            return serial_list
