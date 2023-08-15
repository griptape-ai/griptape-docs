Griptape provides a way to build drivers for vector DBs where embeddings can be stored and queried. Every vector store driver implements the following methods:

* `upsert_text_artifact()` for updating or inserting a new `TextArtifact` into vector DBs. The method will automatically generate embeddings for a given value.
* `upsert_text_artifacts()` for updating or inserting multiple `TextArtifact`s into vector DBs. The method will automatically generate embeddings for given values.
* `upsert_text()` for updating and inserting new arbitrary strings into vector DBs. The method will automatically generate embeddings for a given value.
* `upsert_vector()` for updating and inserting new vectors directly.
* `query()` for querying vector DBs.

Each vector driver takes a `BaseEmbeddingDriver` used to dynamically generate embeddings for strings.

!!! info
    More vector drivers are coming soon.

## LocalVectorStoreDriver

This driver can be used to load and query data from memory. Here is a complete example of how the driver can be used to load a webpage into the driver and query it later:

```python
from griptape.artifacts import BaseArtifact
from griptape.drivers import LocalVectorStoreDriver
from griptape.loaders import WebLoader


vector_store_driver = LocalVectorStoreDriver()
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

## PineconeVectorStoreDriver

This driver supports the [Pinecone vector database](https://www.pinecone.io/). In addition to standard vector driver methods it provides the `create_index()` for easy index creation.

Here is a complete example of how the driver can be used to load and query information from Pinecone:

```python
import hashlib
import json
from urllib.request import urlopen
from decouple import config
from griptape.drivers import PineconeVectorStoreDriver


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
                "rating": product["rating"]
            },
            namespace="supermarket-products"
        )

vector_store_driver = PineconeVectorStoreDriver(
    api_key=config("PINECONE_API_KEY"),
    environment=config("PINECONE_ENVIRONMENT"),
    index_name="griptape-dev"
)

load_data(vector_store_driver)

vector_store_driver.query(
    "fruit",
    count=3,
    filter={
        "price": {"$lte": 15},
        "rating": {"$gte": 4}
    },
    namespace="supermarket-products"
)
```

## MarqoVectorStoreDriver

This driver supports the Marqo vector database. In addition to standard vector driver methods, it also provides the `create_index()`, `delete_index()`, `set_index()`, and `get_indexes()` methods for easy index management.

Here is a complete example of how the driver can be used to load and query information from Marqo:

```python
from griptape import utils
from griptape.drivers import MarqoVectorStoreDriver
from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader
from griptape.structures import Agent
from griptape.tools import KnowledgeBaseClient
import openai
from marqo import Client

# Set the OpenAI API key
openai.api_key_path = "../openai_api_key.txt"

# Define the namespace
namespace = "griptape-ai"

# Initialize the vector store driver
vector_store = MarqoVectorStoreDriver(
    api_key=openai.api_key_path,
    url="http://localhost:8882",
    index="chat2",
    mq=Client(api_key="foobar", url="http://localhost:8882")
)

# Initialize the query engine
query_engine = VectorQueryEngine(vector_store_driver=vector_store)

# Initialize the knowledge base tool
kb_tool = KnowledgeBaseClient(
    description="Contains information about the Griptape Framework from www.griptape.ai",
    query_engine=query_engine,
    namespace=namespace
)

# Load artifacts from the web
artifacts = WebLoader(max_tokens=200).load("https://www.griptape.ai")

# Upsert the artifacts into the vector store
vector_store.upsert_text_artifacts({namespace: artifacts,})
result = vector_store.query(query="What is griptape?")
print(result)
```

### Key Methods
The following methods are available in the `MarqoVectorStoreDriver` class:

1. `__init__(self, api_key: str, url: str, mq: marqo.Client, index: str)`: This method initializes the Marqo client with the given API key, url, and index.
2. `set_index(self, index: str)`: Sets the index for the Marqo client. If the index does not exist, it is created.
3. `upsert_text(self, string: str, vector_id: Optional[str] = None, namespace: Optional[str] = None, meta: Optional[dict] = None)`: Inserts a text document into the Marqo index. If a document with the given vector ID already exists, it is updated; otherwise, a new document is inserted.
4. `upsert_text_artifact(self, artifact: TextArtifact, namespace: Optional[str] = None, meta: Optional[dict] = None)`: Inserts a text artifact into the Marqo index. If an artifact with the given vector ID already exists, it is updated; otherwise, a new artifact is inserted.
5. `load_entry(self, vector_id: str, namespace: Optional[str] = None)`: Loads a document entry from the Marqo index based on the vector ID. Returns the loaded Entry if found; otherwise, None is returned.
6. `load_entries(self, namespace: Optional[str] = None)`: Loads all document entries from the Marqo index. Entries can optionally be filtered by namespace.
7. `query(self, query: str, count: Optional[int] = None, namespace: Optional[str] = None, include_vectors: bool = False, include_metadata=True)`: Queries the Marqo index for documents that match the provided query string. The number of results returned can be limited and entries can optionally be filtered by namespace.
8. `create_index(self, name: str)`: Creates a new index in the Marqo client with the given name.
9. `delete_index(self, name: str)`: Deletes an index in the Marqo client with the given name.
10. `get_indexes(self)`: Returns a list of all indexes in the Marqo client.
11. `upsert_vector(self, vector: list[float], vector_id: Optional[str] = None, namespace: Optional[str] = None, meta: Optional[dict] = None)`: Inserts a vector into the Marqo index. If a vector with the given vector ID already exists, it is updated; otherwise, a new vector is inserted. Currently, this function is not implemented and raises an Exception.

## MongoDbAtlasVectorStoreDriver
This driver provides support for storing vector data in a MongoDB Atlas database. The driver includes methods for performing standard vector operations such as inserting, updating, querying, and loading vectors.

Below is a detailed example of how the MongoDbAtlasVectorStoreDriver can be used to interact with a MongoDB Atlas instance:

```python
from griptape.drivers import MongoDbAtlasVectorStoreDriver

# Initialize the vector store driver
vector_store = MongoDbAtlasVectorStoreDriver(
    connection_string="mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>",
    database_name="myDatabase",
    collection_name="myCollection"
)

# Upsert a vector
vector_id = vector_store.upsert_vector(
    vector=[0.1, 0.2, 0.3],
    namespace="myNamespace",
    meta={"info": "sample"}
)

# Load a specific entry by vector ID
entry = vector_store.load_entry(vector_id=vector_id)
print(entry)

# Query the collection
results = vector_store.query(
    query="What is griptape?",
    count=5
)
print(results)
```

## Key Methods
The following methods are available in the MongoDbAtlasVectorStoreDriver class:

1. `__init__(self, connection_string: str, database_name: str, collection_name: str)`: Initializes the MongoClient with the given connection string, database name, and collection name.
2. `get_collection(self) -> Collection`: Returns the MongoDB Collection instance for the specified database and collection name.
3. `upsert_vector(self, vector: list[float], vector_id: Optional[str] = None, namespace: Optional[str] = None, meta: Optional[dict] = None) -> str`: Inserts or updates a vector in the collection. If a vector with the given vector ID already exists, it is updated; otherwise, a new vector is inserted.
4. `load_entry(self, vector_id: str, namespace: Optional[str] = None) -> Optional[BaseVectorStoreDriver.Entry]`: Loads a document entry from the MongoDB collection based on the vector ID. Returns the loaded Entry if found; otherwise, None is returned.
5. `load_entries(self, namespace: Optional[str] = None) -> list[BaseVectorStoreDriver.Entry]`: Loads all document entries from the MongoDB collection. Entries can optionally be filtered by namespace.
6. `query(self, query: str, count: Optional[int] = None, namespace: Optional[str] = None, include_vectors: bool = False, offset: Optional[int] = 0, index: Optional[str] = None) -> list[BaseVectorStoreDriver.QueryResult]`: Queries the MongoDB collection for documents that match the provided query string. Results can be customized based on parameters like count, namespace, inclusion of vectors, offset, and index.
Note: The implementation details such as the structure of the query method can be tailored according to specific use cases and the nature of the stored vectors. In this example, it's assumed that the driver uses an embedding driver to convert query strings into vectors and leverages specific MongoDB features for nearest neighbor search.