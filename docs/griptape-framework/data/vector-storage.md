Griptape provides a way to build drivers for vector DBs where embeddings can be stored and queried. Every vector storage driver implements the following methods:

* `upsert_text_artifact()` for updating and inserting new `TextArtifact` values into vector DBs. The method will automatically generate embeddings for a given value.
* `upsert_text()` for updating and inserting new arbitrary strings into vector DBs. The method will automatically generate embeddings for a given value.
* `upsert_vector()` for updating and inserting new vectors directly.
* `query()` for querying vector DBs.

Each vector driver takes a `BaseEmbeddingDriver` used to dynamically generate embeddings for strings.

## MemoryVectorDriver

This driver can be used to load and query data from memory. Here is a complete example of how the driver can be used to load a webpage into the driver and query it later:

```python
from griptape.artifacts import BaseArtifact
from griptape.drivers import MemoryVectorDriver
from griptape.loaders import WebLoader


vector_driver = MemoryVectorDriver()
artifacts = WebLoader(max_tokens=100).load("https://www.griptape.ai")

[vector_driver.upsert_text_artifact(a, namespace="griptape") for a in artifacts]

results = vector_driver.query(
    "creativity",
    count=3,
    namespace="griptape"
)

values = [BaseArtifact.from_json(r.meta["artifact"]).value for r in results]

print("\n\n".join(values))
```

## PineconeVectorDriver

This driver supports the [Pinecone vector database](https://www.pinecone.io/). In addition to standard vector driver methods it provides the `create_index()` for easy index creation.

Here is a complete example of how the driver can be used to load and query information from Pinecone:

```python
import hashlib
import json
from urllib.request import urlopen
from decouple import config
from griptape.drivers import PineconeVectorDriver


def load_data(driver: PineconeVectorDriver) -> None:
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
                "rating": product["rating"]
            },
            namespace="supermarket-products"
        )

vector_driver = PineconeVectorDriver(
    api_key=config("PINECONE_API_KEY"),
    environment=config("PINECONE_ENVIRONMENT"),
    index_name="griptape-dev"
)

load_data(vector_driver)

vector_driver.query(
    "fruit",
    count=3,
    filter={
        "price": {"$lte": 15},
        "rating": {"$gte": 4}
    },
    namespace="supermarket-products"
)
```