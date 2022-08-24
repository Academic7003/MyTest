from urllib.parse import urlparse
from django.urls import path, include
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from main.api.views import *

urlpatterns = [
    path('create-product/', create_product, name='create-product'),
    # path('create-material/', create_material, name='create-material')


]