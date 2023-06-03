```python
from griptape.drivers import OpenAiPromptDriver
from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader
from griptape.rules import Ruleset, Rule
from griptape.structures import Agent
from griptape.tools import VectorClient
from griptape.utils import Chat


namespace = "physics"

engine = VectorQueryEngine()

artifacts = WebLoader().load(
    "https://en.wikipedia.org/wiki/Physics"
)

engine.insert(artifacts, namespace=namespace)


vector_client_tool = VectorClient(
    description="This vector database contains information about physics. "
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
    tools=[vector_client_tool],
    prompt_driver=OpenAiPromptDriver(temperature=0.5)
)

Chat(agent).start()

```