################################################################################
#
# models.py
#
# This file defines the models for the testprep API.
#
################################################################################


from django.db import models




class Category(models.Model):
    """ Defines the model for a testprep Category. Many tests may be grouped
        under a category, and a category may be associated with many tests.
    """ 

    name = models.CharField(max_length = 40)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    class Meta:
        verbose_name_plural = "categories"
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_categories'),
        ]        


    def __str__(self):
        """Returns a string depiction of the model"""

        return f'{self.name}'


    def as_dict(self):
        """Returns a dictionary version of the model"""

        return {
            'id': self.pk,
            'name': self.name
        }


# Create your models here.
class Test(models.Model):
    """ Defines the model for a testprep Test. Many tests may be grouped
        under a category, and a test can be associated with many categories.
    """ 

    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 100)
    is_published = models.BooleanField(default= False)

    # We only need to put this field on one side of the relationship.
    categories = models.ManyToManyField('Category', related_name = 'tests', blank = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    class Meta:
        verbose_name_plural = "tests"
        constraints = [
            models.UniqueConstraint(fields=['name', 'description'], name='unique_tests'),
        ]


    def __str__(self):
        """Returns a string depiction of the model"""

        return f'{self.name}'


    def as_dict(self):
        """Returns a dictionary version of the model"""

        return {
            'id': self.pk,
            'name': self.name,
            'description': self.name
        }
