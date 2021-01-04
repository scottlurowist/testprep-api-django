################################################################################
#
# serializers.py
#
# This file defines the serializers for the testprep API.
#
################################################################################


from rest_framework import serializers
from .models import Category, Question, Test




class CategoryLiteSerializer(serializers.ModelSerializer):
    """A simple model serializer for TestSerializer so that API calls to tests
       may retrieve the categories associated with a test. A more full-blown
       category serializer appears later."""
    class Meta:
        model = Category
        fields = ['id', 'name'] 


class QuestionSerializer(serializers.ModelSerializer):
    """A simple model serializer for Questions."""
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type', 'test_id' ]              
        

class TestSerializer(serializers.ModelSerializer):
    """A simple model serializer for Tests."""

    categories = CategoryLiteSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=False)

    class Meta:
        model = Test
        fields = ['name', 'description', 'is_published', 'questions', 'categories']  


    def validate_is_published(self, is_published):
        """ Validates that a test may only be published if the test has at least one
            question and that question has at least two choices. """

        # This is a temporary hack until I have the questions and options in place. Then
        # the validation check will do what the docstring states.
        if is_published == True:
            raise serializers.ValidationError('is_published cannot be true at this time.')

        return is_published


class CategorySerializer(serializers.ModelSerializer):
    """A simple model serializer for categories."""

    tests = TestSerializer(many = True, read_only = True)
      
    class Meta:
        model = Category
        fields = ['id', 'name', 'tests']
