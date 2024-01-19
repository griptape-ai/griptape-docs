This example shows how to use one `Agent` to load content into `TaskMemory` and get that content from another `Agent` using `VectorStoreClient`.

The first `Agent` uses a remote vector store (`MongoDbAtlasVectorStoreDriver` in this example) to handle memory operations. The second `Agent` uses the `VectorStoreClient` with the same `MongoDbAtlasVectorStoreDriver` to get the data.

The `MongoDbAtlasVectorStoreDriver` assumes that you have a vector index configured where the path to the content is called `vector`, and the number of dimensions set on the index is `1536`.

```python
import os
from griptape.tools import WebScraper, VectorStoreClient, TaskMemoryClient
from griptape.structures import Agent
from griptape.drivers import AzureOpenAiChatPromptDriver, AzureOpenAiEmbeddingDriver, MongoDbAtlasVectorStoreDriver
from griptape.engines import VectorQueryEngine, PromptSummaryEngine, CsvExtractionEngine, JsonExtractionEngine
from griptape.memory import TaskMemory 
from griptape.artifacts import TextArtifact
from griptape.memory.task.storage import TextArtifactStorage


AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DATABASE_NAME = os.getenv("MONGODB_DATABASE_NAME")
MONGODB_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME")
MONGODB_CONNECTION_STRING = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}/{MONGODB_DATABASE_NAME}"


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

mongo_driver = MongoDbAtlasVectorStoreDriver(
    connection_string=MONGODB_CONNECTION_STRING,
    database_name=MONGODB_DATABASE_NAME,
    collection_name=MONGODB_COLLECTION_NAME,
    embedding_driver=azure_embedding_driver,
)

vector_engine = VectorQueryEngine(
    vector_store_driver=mongo_driver,
    prompt_driver=azure_prompt_driver,
)
vector_store_tool = VectorStoreClient(
    description='Can be used for all user queries',
    query_engine=vector_engine,
    off_prompt=False
)

task_memory = TaskMemory(
    artifact_storages={
        TextArtifact: TextArtifactStorage(
            query_engine=vector_engine,
            summary_engine=PromptSummaryEngine(
                prompt_driver=azure_prompt_driver
            ),
            csv_extraction_engine=CsvExtractionEngine(
                prompt_driver=azure_prompt_driver
            ),
            json_extraction_engine=JsonExtractionEngine(
                prompt_driver=azure_prompt_driver
            )
        ),
    },
)

loader = Agent(
    tools=[
        WebScraper()
    ],
    prompt_driver=azure_prompt_driver,
    embedding_driver=azure_embedding_driver,
    task_memory=task_memory,
)
asker = Agent(
    tools=[
        vector_store_tool
    ],
    prompt_driver=azure_prompt_driver,
    embedding_driver=azure_embedding_driver,
)

if __name__ == "__main__":
    loader.run("Load https://medium.com/enterprise-rag/a-first-intro-to-complex-rag-retrieval-augmented-generation-a8624d70090f")
    asker.run("why is retrieval augmented generation useful?")
```
