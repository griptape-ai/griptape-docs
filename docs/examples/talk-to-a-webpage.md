This example demonstrates how to vectorize a webpage and setup a Griptape agent with rules and the `KnowledgeBase` tool to use it during conversations.

```python
from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader
from griptape.rules import Ruleset, Rule
from griptape.structures import Agent
from griptape.tools import KnowledgeBaseClient
from griptape.utils import Chat


namespace = "physics"

engine = VectorQueryEngine()

artifacts = WebLoader().load(
    "https://en.wikipedia.org/wiki/Physics"
)

engine.vector_store_driver.upsert_text_artifacts(
    {"physics-wiki": artifacts}
)


kb_client = KnowledgeBaseClient(
    description="Contains information about physics. "
                "Use it to answer any physics-related questions.",
    query_engine=engine,
    namespace=namespace
)

agent = Agent(
    rulesets=[
        Ruleset(
            name="Physics Tutor",
            rules=[
                Rule(
                    "Always introduce yourself as a physics tutor"
                ),
                Rule(
                    "Be truthful. Only discuss physics."
                )
            ]
        )
    ],
    tools=[kb_client]
)

Chat(agent).start()
```