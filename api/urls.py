################################################################################
#
# urls.py
#
# This file defines the urls for the testprep API.
#
################################################################################


from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import CategoryViewSet, TestViewSet




# The ViewSets use these routes.
router = DefaultRouter()
router.register('api/v1/categories', CategoryViewSet)
router.register('api/v1/tests', TestViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
