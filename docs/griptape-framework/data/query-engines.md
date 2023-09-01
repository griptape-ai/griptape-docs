## Overview
Query engines are used to search collections of text.

## VectorQueryEngine

Used to query vector storages. You can set a custom `prompt_driver` and `vector_store_driver`. Uses `LocalVectorStoreDriver` by default.

Use the `insert` method to insert `TextArtifact`s into vector storage with an optional `namespace`.

Use the `query` method to query the vector storage.

```python
from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader

engine = VectorQueryEngine()

engine.upsert_text_artifacts(
    WebLoader().load("https://www.griptape.ai"), namespace="griptape"
)

engine.query(
    "what is griptape?",
    namespace="griptape"
)
```
