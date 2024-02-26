## Overview
Query engines are used to search collections of text.

## VectorQueryEngine

Used to query vector storages. You can set a custom [prompt_driver](../../reference/griptape/engines/query/vector_query_engine.md#griptape.engines.query.vector_query_engine.VectorQueryEngine.prompt_driver.md) and [vector_store_driver](../../reference/griptape/engines/query/vector_query_engine.md#griptape.engines.query.vector_query_engine.VectorQueryEngine.vector_store_driver.md). Uses [LocalVectorStoreDriver](../../reference/griptape/drivers/vector/local_vector_store_driver.md) by default.

Use the [upsert_text_artifact](../../reference/griptape/engines/query/vector_query_engine.md#griptape.engines.query.vector_query_engine.VectorQueryEngine.upsert_text_artifact.md) method to insert [TextArtifact](../../reference/griptape/artifacts/text_artifact.md)s into vector storage with an optional `namespace`.

Use the [VectorQueryEngine](../../reference/griptape/engines/query/vector_query_engine.md#griptape.engines.query.vector_query_engine.VectorQueryEngine.query.md) method to query the vector storage.

```python
import os 

from griptape.drivers import AzureOpenAiChatPromptDriver, LocalVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader

# Initialize a prompt driver
prompt_driver = AzureOpenAiChatPromptDriver(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    model="gpt-3.5-turbo-16k",
    azure_deployment=os.environ["AZURE_OPENAI_35_TURBO_16k_DEPLOYMENT_ID"],
    azure_endpoint=os.environ["AZURE_OPENAI_API_BASE"],
)

engine = VectorQueryEngine(
    prompt_driver=prompt_driver,
    vector_store_driver=LocalVectorStoreDriver(embedding_driver=OpenAiEmbeddingDriver())
)

engine.upsert_text_artifacts(
    WebLoader().load("https://www.griptape.ai"), namespace="griptape"
)

engine.query("what is griptape?", namespace="griptape")
```
