Embeddings in Griptape are multidimensional representations of text data. Embeddings carry semantic information, which makes them useful for extracting relevant chunks from large bodies of text for search and querying.

Griptape provides a way to build embedding drivers that are reused in downstream framework components. Every embedding driver has two basic methods that can be used to generate embeddings:

* `embed_text_artifact()` for `TextArtifact`s
* `embed_string()` for any string

## OpenAiEmbeddingDriver

This embedding driver uses [OpenAI Embeddings API](https://platform.openai.com/docs/guides/embeddings) to generate embeddings for texts of arbitrary length. This driver automatically chunks the input text to fit into the token limit.

Here is how you can use it:

```python
from griptape.drivers import OpenAiEmbeddingDriver


OpenAiEmbeddingDriver().embed_string("Hello Griptape!")
```

Which will generate a 1536-dimensional embedding vector:

```
[0.0018219146877527237, 0.00609285244718194, -0.00580900302156806, ...]
```