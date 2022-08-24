from django.contrib import admin
from main.models import *

class AdminWarehouse(admin.ModelAdmin):
    list_display = ('id', 'material', 'remainder')

class AdminMaterial(admin.ModelAdmin):
    list_display = ('id', 'name', 'material', 'quantity')

admin.site.register(ProductModel)
admin.site.register(MaterialModel)
admin.site.register(ProductMaterialsModel, AdminMaterial)
admin.site.register(WareHouseModel, AdminWarehouse)
