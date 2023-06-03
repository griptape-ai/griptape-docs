Query engines are used to search text storages.

## VectorQueryEngine

Used to query vector storages. You can set a custom `prompt_driver` and `vector_storage_driver`. Uses `MemoryVectorStorageDriver` by default.

Use the `insert` method to insert `TextArtifact`s into vector storage with an optional `namespace`.

```python
engine = VectorQueryEngine()

engine.insert(
    WebLoader().load("https://www.griptape.ai"),
    namespace="griptape"
)
```

Use the `query` method to query the vector storage:

```python
engine.query(
    "what is griptape?",
    namespace="griptape"
)
```