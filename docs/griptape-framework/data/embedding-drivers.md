## Overview
Embeddings in Griptape are multidimensional representations of text data. Embeddings carry semantic information, which makes them useful for extracting relevant chunks from large bodies of text for search and querying.

Griptape provides a way to build Embedding Drivers that are reused in downstream framework components. Every Embedding Driver has two basic methods that can be used to generate embeddings:

* [embed_text_artifact()](../../reference/griptape/drivers/embedding/base_embedding_driver.md#griptape.drivers.embedding.base_embedding_driver.BaseEmbeddingDriver.embed_text_artifact) for [TextArtifact](../../reference/griptape/artifacts/text_artifact.md)s
* [embed_string()](../../reference/griptape/drivers/embedding/base_embedding_driver.md#griptape.drivers.embedding.base_embedding_driver.BaseEmbeddingDriver.embed_string) for any string

!!! info
    More embedding drivers are coming soon.

## Embedding Drivers

### OpenAI Embeddings

The [OpenAiEmbeddingDriver](../../reference/griptape/drivers/embedding/openai_embedding_driver.md) uses [OpenAI Embeddings API](https://platform.openai.com/docs/guides/embeddings) to generate embeddings for texts of arbitrary length. This driver automatically chunks the input text to fit into the token limit.

```python
from griptape.drivers import OpenAiEmbeddingDriver

embeddings = OpenAiEmbeddingDriver().embed_string("Hello Griptape!")

# display the first 3 embeddings
print(embeddings[:3])
```
```
[0.0017853748286142945, 0.006118456833064556, -0.005811543669551611]
```

### Azure OpenAI Embeddings

The [AzureOpenAiEmbeddingDriver](../../reference/griptape/drivers/embedding/azure_openai_embedding_driver.md) uses the same parameters as [OpenAiEmbeddingDriver](../../reference/griptape/drivers/embedding/openai_embedding_driver.md)
with updated defaults.

### Bedrock Titan Embeddings
The [BedrockTitanEmbeddingDriver](../../reference/griptape/drivers/embedding/bedrock_titan_embedding_driver.md) uses the [Amazon Bedrock Embeddings API](https://docs.aws.amazon.com/bedrock/latest/userguide/embeddings.html).

```python
from griptape.drivers import BedrockTitanEmbeddingDriver

embeddings = BedrockTitanEmbeddingDriver().embed_string("Hello world!")

# display the first 3 embeddings
print(embeddings[:3])
```
```
[-0.234375, -0.024902344, -0.14941406]
```

### Override Default Structure Embedding Driver
Here is how you can override the Embedding Driver that is used by default in agents. 

```python
from griptape.structures import Agent
from griptape.tools import WebScraper
from griptape.drivers import LocalVectorStoreDriver, OpenAiEmbeddingDriver

agent = Agent(
    tools=[WebScraper()],
    embedding_driver=OpenAiEmbeddingDriver()
)

agent.run("based on https://www.griptape.ai/, tell me what Griptape is")
```
