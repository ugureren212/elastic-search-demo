import random
from django.core.management.base import BaseCommand
from api.models import Product  # Import your Product model

class Command(BaseCommand):
    help = "Create 1,000,000 new products in the database"

    def handle(self, *args, **kwargs):
        products = []
        for i in range(1000000):
            product_name = f"Product {i+1}"
            description = f"This is the description for {product_name}."
            price = round(random.uniform(10, 500), 2)  # Random price between 10 and 500
            stock = random.randint(1, 100)  # Random stock between 1 and 100
            products.append(Product(name=product_name, description=description, price=price, stock=stock))

        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS("Successfully created 1000 products!"))
