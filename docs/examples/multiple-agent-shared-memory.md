This example shows how to use one `Agent` to load content into `TaskMemory` and get that content from another `Agent` using `VectorStoreClient`.

The first `Agent` uses a remote vector store (`MongoDbAtlasVectorStoreDriver` in this example) to handle memory operations. The second `Agent` uses the `VectorStoreClient` with the same `MongoDbAtlasVectorStoreDriver` to get the data.

The `MongoDbAtlasVectorStoreDriver` assumes that you have a vector index configured where the path to the content is called `vector`, and the number of dimensions set on the index is `1536`.

```python
from dotenv import load_dotenv
from griptape.tools import WebScraper, VectorStoreClient, TaskMemoryClient
from griptape.structures import Agent
from griptape.drivers import AzureOpenAiChatPromptDriver, AzureOpenAiEmbeddingDriver, MongoDbAtlasVectorStoreDriver
from griptape.engines import VectorQueryEngine, PromptSummaryEngine, CsvExtractionEngine, JsonExtractionEngine
from griptape.memory import TaskMemory
from griptape.artifacts import TextArtifact
from griptape.memory.task.storage import TextArtifactStorage

import os

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

MONGO_CONNECTION_STRING = os.getenv('MONGO_CONNECTION_STRING')
MONGO_DATABASE_NAME = os.getenv('MONGO_DATABASE_NAME')
MONGO_COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME')


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
    connection_string=MONGO_CONNECTION_STRING,
    database_name=MONGO_DATABASE_NAME,
    collection_name=MONGO_COLLECTION_NAME,
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
    loader.run("Load https://griptape.ai")
    asker.run("What is griptape?")
```