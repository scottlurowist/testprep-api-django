################################################################################
#
# serializers.py
#
# This file defines the serializers for the testprep API.
#
################################################################################


from rest_framework import serializers
from .models import Category, Test




class CategoryLiteSerializer(serializers.ModelSerializer):
    """A simple model serializer for TestSerializer so that API calls to tests
       may retrieve the categories associated with a test. A more full-blown
       category serializer appears later."""
    class Meta:
        model = Category
        fields = ['id', 'name']      


class TestSerializer(serializers.ModelSerializer):
    """A simple model serializer for Tests."""

    categories = CategoryLiteSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ['name', 'description', 'categories']  


class CategorySerializer(serializers.ModelSerializer):
    """A simple model serializer for categories."""

    tests = TestSerializer(many = True, read_only = True)
      
    class Meta:
        model = Category
        fields = ['id', 'name', 'tests']


      
