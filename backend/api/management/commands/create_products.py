import random
from django.core.management.base import BaseCommand
from api.models import Product

class Command(BaseCommand):
    help = "Create 10,000 new products in the database with extended fields"

    def handle(self, *args, **kwargs):
        categories = ["Electronics", "Fashion", "Home", "Books", "Sports", "Toys"]
        brands = ["BrandA", "BrandB", "BrandC", "BrandD", "BrandE"]
        colors = ["Red", "Blue", "Green", "Black", "White", "Yellow"]
        ratings = [1, 2, 3, 4, 5]
        availability = [True, False]

        products = []
        for i in range(10000):
            product_name = f"Product {i+1}"
            description = f"This is the description for {product_name}."
            price = round(random.uniform(10, 500), 2)
            stock = random.randint(1, 100)
            category = random.choice(categories)
            brand = random.choice(brands)
            color = random.choice(colors)
            rating = random.choice(ratings)
            is_available = random.choice(availability)

            product = Product(
                name=product_name,
                description=description,
                price=price,
                stock=stock,
                category=category,
                brand=brand,
                color=color,
                rating=rating,
                is_available=is_available,
            )
            products.append(product)

            if len(products) >= 10000:
                Product.objects.bulk_create(products)
                products = []

        if products:
            Product.objects.bulk_create(products)

        self.stdout.write(self.style.SUCCESS("10,000 products created successfully!"))
