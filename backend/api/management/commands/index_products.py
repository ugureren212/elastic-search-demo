from django.core.management.base import BaseCommand
from api.models import Product
from api.utils.elasticsearch_client import es  # Import the shared Elasticsearch client

class Command(BaseCommand):
    help = "Index products to Elasticsearch"

    def handle(self, *args, **kwargs):
        index_name = "products"
        products = Product.objects.all()

        for product in products:
            es.index(
                index=index_name,
                id=product.id,
                body={
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "stock": product.stock,
                }
            )
        self.stdout.write("Products indexed successfully!")
