from main.models import *
from rest_framework.response import Response
from main.api.serilaizers import *
from rest_framework import status
from rest_framework.decorators import api_view


def create_product(request):
    serializer = ProductSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create_material(request):
    serializer = MaterialSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

