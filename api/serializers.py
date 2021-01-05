################################################################################
#
# serializers.py
#
# This file defines the serializers for the testprep API.
#
################################################################################


from rest_framework import serializers
from .models import Category, Question, Test
from datetime import datetime
from django.db import transaction
from django.db.utils import DatabaseError, IntegrityError





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

    categories = CategoryLiteSerializer(many=True)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ['id', 'name', 'description', 'is_published', 'questions', 'categories']  


    def validate_is_published(self, is_published):
        """ Validates that a test may only be published if the test has at least one
            question and that question has at least two choices. """

        # This is a temporary hack until I have the questions and options in place. Then
        # the validation check will do what the docstring states.
        if is_published == True:
            raise serializers.ValidationError('is_published cannot be true at this time.')

        return is_published


    def create(self, validated_data):
        """ Overrides create since we are dealing with a many-to-many
            relationship. We must first save the test than the questions
            before we can establish the many-to-many relationship. """

        validated_data_to_return = validated_data

        categories_data = validated_data['categories']
        questions_data = validated_data['questions']

        current_date_time = datetime.now()

        try:
            with transaction.atomic():

                # Create the test before we can associate the test with the 
                # categories. 
                new_test = Test.objects.create(
                    name = validated_data['name'], 
                    description = validated_data['description'],
                    is_published = validated_data['is_published'],
                    created_at = current_date_time,
                    updated_at = current_date_time)

                # Update the many-to-many table with the new test.
                for category in categories_data:
                    cat = Category.objects.get(name = category['name'])   
                    new_test.categories.add(cat)

                # Persist each question.
                for question in questions_data:
                    current_date_time = datetime.now()
                    Question.objects.create(
                        created_at = current_date_time,
                        updated_at = current_date_time,
                        question_text =  question['question_text'],
                        question_type = question['question_type'],
                        test_id = new_test.id)
        except IntegrityError as integrity_error:
            raise serializers.ValidationError(f'The POST failed - {integrity_error}')                        
        except DatabaseError as generic_db_error:
            raise serializers.ValidationError(f'{generic_db_error}')
        else:
            return new_test


class CategorySerializer(serializers.ModelSerializer):
    """A simple model serializer for categories."""

    tests = TestSerializer(many = True, read_only = True)
      
    class Meta:
        model = Category
        fields = ['id', 'name', 'tests']
