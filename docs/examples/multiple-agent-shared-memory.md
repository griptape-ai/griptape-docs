This example shows how to use one `Agent` to load content into `TaskMemory` and get that content from another `Agent` using `TaskMemoryClient`.

The first `Agent` uses a remote vector store (`MongoDbAtlasVectorStoreDriver` in this example) to handle memory operations. The second `Agent` uses the same instance of `TaskMemory` and the `TaskMemoryClient` with the same `MongoDbAtlasVectorStoreDriver` to get the data.

The `MongoDbAtlasVectorStoreDriver` assumes that you have a vector index configured where the path to the content is called `vector`, and the number of dimensions set on the index is `1536` (this is a commonly used number of dimensions for embedding models).

`asker` uses the same instance of `TaskMemory` as `loader` so that `asker` has access to the `namespace_storages` that `loader` has set.

```python
import os
from griptape.tools import WebScraper, VectorStoreClient, TaskMemoryClient
from griptape.structures import Agent
from griptape.drivers import AzureOpenAiChatPromptDriver, AzureOpenAiEmbeddingDriver, AzureMongoDbVectorStoreDriver
from griptape.engines import VectorQueryEngine, PromptSummaryEngine, CsvExtractionEngine, JsonExtractionEngine
from griptape.memory import TaskMemory 
from griptape.artifacts import TextArtifact
from griptape.memory.task.storage import TextArtifactStorage
from griptape.config import StructureConfig, StructureGlobalDriversConfig


AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_API_BASE")

MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DATABASE_NAME = os.getenv("MONGODB_DATABASE_NAME")
MONGODB_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")
MONGODB_INDEX_NAME = os.getenv("MONGODB_INDEX_NAME")
MONGODB_VECTOR_PATH = os.getenv("MONGODB_VECTOR_PATH")
MONGODB_CONNECTION_STRING = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}/{MONGODB_DATABASE_NAME}?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"


azure_embedding_driver = AzureOpenAiEmbeddingDriver(
    model='text-embedding-ada-002',
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment='text-embedding-ada-002'
)

azure_prompt_driver = AzureOpenAiChatPromptDriver(
    model='gpt-4',
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment='gpt-4'
)

mongo_driver = AzureMongoDbVectorStoreDriver(
    connection_string=MONGODB_CONNECTION_STRING,
    database_name=MONGODB_DATABASE_NAME,
    collection_name=MONGODB_COLLECTION_NAME,
    embedding_driver=azure_embedding_driver,
    index_name=MONGODB_INDEX_NAME,
    vector_path=MONGODB_VECTOR_PATH
)

loader = Agent(
    tools=[
        WebScraper()
    ],
    config=StructureConfig(
        global_drivers=StructureGlobalDriversConfig(
            prompt_driver=azure_prompt_driver,
            vector_store_driver=mongo_driver,
            embedding_driver=azure_embedding_driver
        )
    ),
)
asker = Agent(
    tools=[
        TaskMemoryClient(off_prompt=False),
    ],
    meta_memory=loader.meta_memory,
    task_memory=loader.task_memory,
)

if __name__ == "__main__":
    loader.run("Load https://medium.com/enterprise-rag/a-first-intro-to-complex-rag-retrieval-augmented-generation-a8624d70090f")
    asker.run("why is retrieval augmented generation useful?")
```
