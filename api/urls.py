from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet, BrandViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('brands', BrandViewSet)

urlpatterns = [
    path('', include(router.urls)),
]