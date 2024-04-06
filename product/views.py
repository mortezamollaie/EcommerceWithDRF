from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category
from .serializers import CategorySerializers


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializers)
    def list(self, request):
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data)
