This tool enables LLMs to dynamically query vector DBs.

The `VectorStorageClient` tool uses the following parameters:

| Parameter     | Description                              | Required |
|---------------|------------------------------------------|----------|
| description   | LLM-friendly vector storage description  | NO       |
| namespace     | Vector storage namespace                 | NO       |
| driver_class  | Vector storage driver class              | YES      |
| driver_fields | Vector storage driver constructor fields | NO       |

Here is an end-to-end example of how it can be used with the Pincone storage driver:

```python
from decouple import config
from griptape.drivers import OpenAiPromptDriver
from griptape.structures import Agent
from griptape.tasks import ToolkitTask
from griptape.tools import VectorStorageClient


pinecone = VectorStorageClient(
    description="This vector database contains information about "
                "various products at the supermarket. Searching it "
                "returns a product description, title, type, rating, and price",
    driver_class="PineconeVectorStorageDriver",
    driver_fields={
        "api_key": config("PINECONE_API_KEY"),
        "environment": config("PINECONE_ENVIRONMENT"),
        "index_name": "griptape-dev"
    },
    namespace="supermarket-products"
)

agent = Agent(
    tools=[pinecone]
)

agent.run(
    "find deserts"
)
```