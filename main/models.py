from django.db import models


class Xomashyo(models.Model):
    name = models.TextField()
    kod = models.IntegerField()

class Mahsulot(models.Model):
    name = models.TextField()

class MahXom(models.Model):
    name = models.OneToOneField(Mahsulot, on_delete=models.CASCADE)
    xomashyo = models.ForeignKey(Xomashyo, on_delete=models.CASCADE)

