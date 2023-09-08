This tool enables LLMs to dynamically query tool memory.

The `VectorStoreClient` tool uses the following parameters:

| Parameter    | Description                                               | Required |
|--------------|-----------------------------------------------------------|----------|
| description  | LLM-friendly vector DB description                        | YES      |
| namespace    | Vector storage namespace                                  | NO       |
| query_engine | `BaseQueryEngine`                                         | YES      |
| top_n        | Max number of results returned for the query engine query | NO       |

Here is an example of how it can be used with the Pincone storage driver:

```python
from griptape.structures import Agent
from griptape.tools import VectorStoreClient
from griptape.loaders import WebLoader
from griptape.engines import VectorQueryEngine


engine = VectorQueryEngine()

engine.upsert_text_artifacts(
    WebLoader().load("https://www.griptape.ai"),
    namespace="griptape"
)
    
vector_db = VectorStoreClient(
    description="This DB has information about the Griptape Python framework",
    query_engine=engine,
    namespace="griptape"
)

agent = Agent(
    tools=[vector_db]
)

agent.run(
    "what is Griptape?"
)
```
