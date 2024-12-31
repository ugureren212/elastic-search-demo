from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).resolve().parents[3] / "elastic-start-local/.env"
print("env_path: ", env_path)
load_dotenv(dotenv_path=env_path)

# Get the Elasticsearch password from environment variables
es_local_password = os.getenv("ES_LOCAL_PASSWORD")

# Elasticsearch client instance
es = Elasticsearch(
    hosts=["http://localhost:9200"],
    basic_auth=("elastic", es_local_password)
)
