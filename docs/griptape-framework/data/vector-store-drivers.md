## Overview

Griptape provides a way to build drivers for vector DBs where embeddings can be stored and queried. Every vector store driver implements the following methods:

- `upsert_text_artifact()` for updating or inserting a new [TextArtifact](../../reference/griptape/artifacts/text_artifact.md) into vector DBs. The method will automatically generate embeddings for a given value.
- `upsert_text_artifacts()` for updating or inserting multiple [TextArtifact](../../reference/griptape/artifacts/text_artifact.md)s into vector DBs. The method will automatically generate embeddings for given values.
- `upsert_text()` for updating and inserting new arbitrary strings into vector DBs. The method will automatically generate embeddings for a given value.
- `upsert_vector()` for updating and inserting new vectors directly.
- `query()` for querying vector DBs.
- `create_index()`: For easy index creation.

Each vector driver takes a [BaseEmbeddingDriver](../../reference/griptape/drivers/embedding/base_embedding_driver.md) used to dynamically generate embeddings for strings.

!!! info
    More vector drivers are coming soon.

## Local Vector Store Driver

The [LocalVectorStoreDriver](../../reference/griptape/drivers/vector/local_vector_store_driver.md) can be used to load and query data from memory. Here is a complete example of how the driver can be used to load a webpage into the driver and query it later:

```python
import os 
from griptape.artifacts import BaseArtifact
from griptape.drivers import LocalVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.loaders import WebLoader


# Initialize an embedding driver
embedding_driver = OpenAiEmbeddingDriver(api_key=os.getenv("OPENAI_API_KEY"))

vector_store_driver = LocalVectorStoreDriver(embedding_driver=embedding_driver)
artifacts = WebLoader(max_tokens=100).load("https://www.griptape.ai")

[vector_store_driver.upsert_text_artifact(a, namespace="griptape") for a in artifacts]

results = vector_store_driver.query(
    "creativity",
    count=3,
    namespace="griptape"
)

values = [BaseArtifact.from_json(r.meta["artifact"]).value for r in results]

print("\n\n".join(values))

```

## Pinecone Vector Store Driver

The [PineconeVectorStoreDriver](../../reference/griptape/drivers/vector/pinecone_vector_store_driver.md) supports the [Pinecone vector database](https://www.pinecone.io/).

Here is an example of how the driver can be used to load and query information in a Pinecone cluster:

```python
import os
import hashlib
import json
from urllib.request import urlopen
from griptape.drivers import PineconeVectorStoreDriver, OpenAiEmbeddingDriver

def load_data(driver: PineconeVectorStoreDriver) -> None:
    response = urlopen(
        "https://raw.githubusercontent.com/wedeploy-examples/"
        "supermarket-web-example/master/products.json"
    )

    for product in json.loads(response.read()):
        driver.upsert_text(
            product["description"],
            vector_id=hashlib.md5(product["title"].encode()).hexdigest(),
            meta={
                "title": product["title"],
                "description": product["description"],
                "type": product["type"],
                "price": product["price"],
                "rating": product["rating"],
            },
            namespace="supermarket-products",
        )

# Initialize an embedding driver
embedding_driver = OpenAiEmbeddingDriver(api_key=os.getenv("OPENAI_API_KEY"))

vector_store_driver = PineconeVectorStoreDriver(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENVIRONMENT"),
    index_name=os.getenv('PINECONE_INDEX_NAME'),
    embedding_driver=embedding_driver,
)

load_data(vector_store_driver)

result = vector_store_driver.query(
    "fruit",
    count=3,
    filter={"price": {"$lte": 15}, "rating": {"$gte": 4}},
    namespace="supermarket-products",
)
```

## Marqo Vector Store Driver

The [MarqoVectorStoreDriver](../../reference/griptape/drivers/vector/marqo_vector_store_driver.md) supports the Marqo vector database.

Here is an example of how the driver can be used to load and query information in a Marqo cluster:

```python
import os
from griptape.drivers import MarqoVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader
from griptape.tools import VectorStoreClient

# Initialize an embedding driver
embedding_driver = OpenAiEmbeddingDriver(api_key=os.getenv("OPENAI_API_KEY"))

# Define the namespace
namespace = 'griptape-ai'

# Initialize the vector store driver
vector_store = MarqoVectorStoreDriver(
    api_key=os.getenv("MARQO_API_KEY"),
    url=os.getenv("MARQO_URL"),
    index=os.getenv("MARQO_INDEX_NAME"),
    embedding_driver=embedding_driver,
)

# Initialize the query engine
query_engine = VectorQueryEngine(vector_store_driver=vector_store)

# Initialize the knowledge base tool
VectorStoreClient(
    description="Contains information about the Griptape Framework from www.griptape.ai",
    query_engine=query_engine,
    namespace=namespace,
)

# Load artifacts from the web
artifacts = WebLoader(max_tokens=200).load("https://www.griptape.ai")

# Upsert the artifacts into the vector store
vector_store.upsert_text_artifacts(
    {
        namespace: artifacts,
    }
)
result = vector_store.query(query="What is griptape?")
print(result)
```

## Mongodb Atlas Vector Store Driver

The [MongodbAtlasVectorStoreDriver](../../reference/griptape/drivers/vector/mongodb_vector_store_driver.md) provides support for storing vector data in a MongoDB Atlas database.

Here is an example of how the driver can be used to load and query information in a MongoDb Atlas Cluster:

```python
from griptape.drivers import MongoDbAtlasVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.loaders import WebLoader
import os

# Initialize an embedding driver
embedding_driver = OpenAiEmbeddingDriver(api_key=os.getenv("OPENAI_API_KEY"))

host = os.getenv("MONGODB_HOST")
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")
database_name = os.getenv("MONGODB_DATABASE_NAME")
collection_name = os.getenv("MONGODB_COLLECTION_NAME")
# Initialize the vector store driver
vector_store = MongoDbAtlasVectorStoreDriver(
    connection_string=f"mongodb+srv://{username}:{password}@{host}/{database_name}",
    database_name=database_name,
    collection_name=collection_name,
    embedding_driver=embedding_driver,
)

# Load artifacts from the web
artifacts = WebLoader(max_tokens=200).load("https://www.griptape.ai")

# Upsert the artifacts into the vector store
vector_store.upsert_text_artifacts(
    {
        "griptape": artifacts,
    }
)

result = vector_store.query(query="What is griptape?")
print(result)
```

## Redis Vector Store Driver

The [RedisVectorStoreDriver](../../reference/griptape/drivers/vector/redis_vector_store_driver.md) integrates with the Redis vector storage system.

Here is an example of how the driver can be used to load and query information in a Redis Cluster:

```python
import os
from griptape.drivers import RedisVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.loaders import WebLoader
import numpy as np  # Assuming you'd use numpy to create a dummy vector for the sake of example.

# Initialize an embedding driver
embedding_driver = OpenAiEmbeddingDriver(api_key=os.getenv("OPENAI_API_KEY"))

vector_store_driver = RedisVectorStoreDriver(
    host=os.getenv("REDIS_HOST"),
    port=os.getenv("REDIS_PORT"),
    password=os.getenv("REDIS_PASSWORD"),
    index=os.getenv("REDIS_INDEX"),
    embedding_driver=embedding_driver,
)

# Load artifacts from the web
artifacts = WebLoader(max_tokens=200).load("https://www.griptape.ai")

# Upsert the artifacts into the vector store
vector_store_driver.upsert_text_artifacts(
    {
        "griptape": artifacts,
    }
)

result = vector_store_driver.query(query="What is griptape?")
print(result)
```

## OpenSearch Vector Store Driver

The [OpenSearchVectorStoreDriver](../../reference/griptape/drivers/vector/opensearch_vector_store_driver.md) integrates with the OpenSearch platform, allowing for storage, retrieval, and querying of vector data.

Here is an example of how the driver can be used to load and query information in an OpenSearch Cluster:

```python
import os
import boto3
from griptape.drivers import AmazonOpenSearchVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.loaders import WebLoader

# Initialize an embedding driver
embedding_driver = OpenAiEmbeddingDriver(api_key=os.getenv("OPENAI_API_KEY"))

vector_store_driver = AmazonOpenSearchVectorStoreDriver(
    host=os.getenv("AMAZON_OPENSEARCH_HOST"),
    index_name=os.getenv("AMAZON_OPENSEARCH_INDEX_NAME"),
    session=boto3.Session(),
    embedding_driver=embedding_driver,
)

# Load artifacts from the web
artifacts = WebLoader(max_tokens=200).load("https://www.griptape.ai")

# Upsert the artifacts into the vector store
vector_store_driver.upsert_text_artifacts(
    {
        "griptape": artifacts,
    }
)

result = vector_store_driver.query(query="What is griptape?")

print(result)
```

## PGVector Vector Store Driver

The [PGVectorVectorStoreDriver](../../reference/griptape/drivers/vector/pgvector_vector_store_driver.md) integrates with PGVector, a vector storage and search extension for Postgres. While Griptape will handle enabling the extension, PGVector must be installed and ready for use in your Postgres instance before using this vector store driver.

Here is an example of how the driver can be used to load and query information in a Postgres database:

```python 
import os 
from griptape.drivers import PgVectorVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.loaders import WebLoader

# Initialize an embedding driver.
embedding_driver = OpenAiEmbeddingDriver(api_key=os.getenv("OPENAI_API_KEY"))

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_connection_string = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
vector_store_driver = PgVectorVectorStoreDriver(
    connection_string=db_connection_string,
    embedding_driver=embedding_driver,
    table_name="griptape_vectors",
)

# Install required Postgres extensions and create database schema.
vector_store_driver.setup()

web_loader = WebLoader()
artifacts = web_loader.load("https://www.griptape.ai")
vector_store_driver.upsert_text_artifacts(
    {
        "griptape": artifacts,
    }
)

result = vector_store_driver.query("What is griptape?")
print(result)
```
