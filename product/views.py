from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product
from .serializers import CategorySerializers, BrandSerializers, ProductSerializers


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializers)
    def list(self, request):
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
        A simple Viewset for viewing brands
        """
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializers)
    def list(self, request):
        serializer = BrandSerializers(self.queryset, many=True)
        return Response(serializer.data)

