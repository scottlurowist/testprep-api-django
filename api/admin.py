################################################################################
#
# admin.py
#
# This file registers the models for use in the Django admin portal.
#
################################################################################


from django.contrib import admin
from .models import Test, Category




# Register your models here.
admin.site.register(Category)
admin.site.register(Test)