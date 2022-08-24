from pyexpat import model
from django.db import models


class MaterialModel(models.Model):
    name = models.TextField()
    kod = models.IntegerField()

    def __str__(self):
        return str(self.name)
    
    

class ProductModel(models.Model):
    name = models.TextField()

    def __str__(self):
        return str(self.name)



class ProductMaterialsModel(models.Model):
    name = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    material = models.ForeignKey(MaterialModel, related_name='kerak', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.name)

class WareHouseModel(models.Model):
    material = models.ForeignKey(MaterialModel, on_delete=models.CASCADE, )
    remainder = models.BigIntegerField()
    price = models.BigIntegerField()
    
    def __str__(self):
        return str(f"{self.material}")

