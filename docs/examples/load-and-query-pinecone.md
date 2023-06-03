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
    index_name=config("PINECONE_INDEX_NAME")
)

load_data(vector_driver)

result = vector_driver.query(
    "fruit",
    count=3,
    filter={
        "price": {"$lte": 15},
        "rating": {"$gte": 4}
    },
    namespace="supermarket-products"
)

print(result)
```