from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SearchProductsView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('products/search/', SearchProductsView.as_view(), name='search-products'),
    path('', include(router.urls)),
]
