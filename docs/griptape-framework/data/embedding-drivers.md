## Overview
Embeddings in Griptape are multidimensional representations of text data. Embeddings carry semantic information, which makes them useful for extracting relevant chunks from large bodies of text for search and querying.

Griptape provides a way to build Embedding Drivers that are reused in downstream framework components. Every Embedding Driver has two basic methods that can be used to generate embeddings:

* [embed_text_artifact()](../../reference/griptape/drivers/embedding/base_embedding_driver.md#griptape.drivers.embedding.base_embedding_driver.BaseEmbeddingDriver.embed_text_artifact) for [TextArtifact](../../reference/griptape/artifacts/text_artifact.md)s
* [embed_string()](../../reference/griptape/drivers/embedding/base_embedding_driver.md#griptape.drivers.embedding.base_embedding_driver.BaseEmbeddingDriver.embed_string) for any string

!!! info
    More embedding drivers are coming soon.

## OpenAI Embeddings

The [OpenAiEmbeddingDriver](../../reference/griptape/drivers/embedding/openai_embedding_driver.md) uses [OpenAI Embeddings API](https://platform.openai.com/docs/guides/embeddings) to generate embeddings for texts of arbitrary length. This driver automatically chunks the input text to fit into the token limit.

Here is how you can use it:

```python
>>> from griptape.drivers import OpenAiEmbeddingDriver

>>> OpenAiEmbeddingDriver().embed_string("Hello Griptape!")
[0.0018212645081803203, 0.006074181292206049, -0.005777235608547926, ...]

```

## Azure OpenAI Embeddings

The [AzureOpenAiEmbeddingDriver](../../reference/griptape/drivers/embedding/azure_openai_embedding_driver.md) uses the same parameters as [OpenAiEmbeddingDriver](../../reference/griptape/drivers/embedding/openai_embedding_driver.md)
with updated defaults.
