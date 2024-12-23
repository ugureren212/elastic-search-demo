from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        data = {"message": "Hello, World!"}
        return Response(data)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
