import os
from dotenv import load_dotenv
from pathlib import Path
from elasticsearch import Elasticsearch
from api.models import Product

env_path = Path(__file__).resolve().parents[3] / "elastic-start-local/.env"


load_dotenv(dotenv_path=env_path)

es_local_password = os.getenv("ES_LOCAL_PASSWORD")

# Initialize Elasticsearch client
es = Elasticsearch(
    hosts=["http://localhost:9200"],
    basic_auth=("elastic", es_local_password)  # Use the password from .env
)

# Index name
index_name = "products"

def index_products():
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
    print("Products indexed successfully!")


if __name__ == "__main__":
    index_products()
