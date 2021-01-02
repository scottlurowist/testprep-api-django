################################################################################
#
# views.py
#
# This file defines the views for the testprep API.
#
################################################################################


from django.shortcuts import render
from rest_framework import views, viewsets, generics
from rest_framework.response import Response
from rest_framework import status 
from .models import Category, Test
from .serializers import CategorySerializer, TestSerializer




# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """A Viewset that exposes the Categories endpoint."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TestViewSet(viewsets.ModelViewSet):
    """A Viewset that exposes the Tests endpoint."""  

    queryset = Test.objects.all()
    serializer_class = TestSerializer
   