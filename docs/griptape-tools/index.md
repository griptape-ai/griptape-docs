Tools give the LLM abilities to invoke outside APIs, reference data sets, and generally expand their capabilities.

Agents (or any other structure for that matter) can be used to connect your pre-processed data to LLMs via tools. Griptape tools are Python classes with activities. Activities are Python methods decorated with the @activity decorator. Each activity has a description (used to provide context to the LLM) and the input schema that the LLM must follow in order to use the tool. Griptape validates LLM outputs against the schema to ensure each tool activity is used correctly.

We provide a set of official Griptape Tools for accessing and processing data. You can also build tools yourself. For example, here is a simple tool for generating random numbers:

```python
import random
from griptape.artifacts import TextArtifact
from griptape.core import BaseTool
from griptape.core.decorators import activity
from schema import Schema, Literal, Optional


class RandomNumberGenerator(BaseTool):
    @activity(config={
            "description": "Can be used to generate random numbers",
            "schema": Schema({
                Optional(Literal(
                    "decimals",
                    description="Number of decimals to round the random number to"
                )): int
            })
        })
    def generate(self, params: dict) -> TextArtifact:
        return TextArtifact(
            str(round(random.random(), params["values"].get("decimals")))
        )
```

Now, let’s build an agent that accesses pre-processed webpage data from the previous example via tools:
```python
from griptape import utils
from griptape.drivers import LocalVectorStoreDriver
from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader
from griptape.structures import Agent
from griptape.tools import VectorStoreClient

namespace = "griptape-ai"
vector_store = LocalVectorStoreDriver()
query_engine = VectorQueryEngine(
    vector_store_driver=vector_store
)
vector_store_tool = VectorStoreClient(
    description="Contains information about the Griptape Framework "
                "from www.griptape.ai",
    query_engine=query_engine,
    namespace=namespace
)
artifacts = WebLoader(max_tokens=100).load("https://www.griptape.ai")

vector_store.upsert_text_artifacts({
    namespace: artifacts,
})

agent = Agent(tools=[vector_store_tool])

utils.Chat(agent).start()
```
Here we instantiate the VectorStoreClient tool that wraps the query engine and enables the LLM to search knowledge bases. We then initialize an agent with that tool and start a CLI chat.

Upon initialization, agents instantiate conversation memory[](../griptape-framework/structures/conversation-memory.md) used to preserve the conversation flow. Griptape supports different types of conversation memory, such as **BufferConversationMemory** and **SummaryConversationMemory**, which are useful in different scenarios.

