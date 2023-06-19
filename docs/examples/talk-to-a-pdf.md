This example demonstrates how to vectorize a PDF of the [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf) paper and setup a Griptape agent with rules and the `KnowledgeBase` tool to use it during conversations.

```python
import io
import requests
from griptape.engines import VectorQueryEngine
from griptape.loaders import PdfLoader
from griptape.structures import Agent
from griptape.tools import KnowledgeBaseClient
from griptape.utils import Chat

namespace = "attention"

response = requests.get("https://arxiv.org/pdf/1706.03762.pdf")
engine = VectorQueryEngine()

engine.vector_store_driver.upsert_text_artifacts(
    {
        "attention-paper": PdfLoader().load(
            io.BytesIO(response.content)
        )
    }
)

kb_client = KnowledgeBaseClient(
    description="Contains information about the Attention Is All You Need paper. "
                "Use it to answer any any related questions.",
    query_engine=engine,
    namespace=namespace
)

agent = Agent(
    tools=[kb_client]
)

Chat(agent).start()
```