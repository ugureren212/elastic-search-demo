from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from backend.services.elasticsearch_client import es
from .models import Product
from .serializers import ProductSerializer

class SearchProductsView(APIView):

    def get(self, request):
        query = request.GET.get("q", "").strip()

        if not query:
            return Response(
                {"error": "Query parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Perform the search query in Elasticsearch
            result = es.search(
                index="products",
                query={
                    "match": {
                        "name": query  # Search for products by the "name" field
                    }
                }
            )

            # Extract hits from the result
            hits = result["hits"]["hits"]
            products = [{"id": hit["_id"], **hit["_source"]} for hit in hits]

            return Response(products, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
