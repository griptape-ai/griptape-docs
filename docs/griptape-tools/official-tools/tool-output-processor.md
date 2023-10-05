# ToolOutputProcessor

This tool enables LLMs to query, extract, and summarize tool outputs via shared short-term tool memory. Before using it, you'll likely want to disable all memory activities, so the LLM doesn't get confused which one to use. THis tool is helpful when you want the queried memory output to go back to memory.

```python
from griptape.structures import Agent
from griptape.tools import ToolOutputProcessor
from griptape.memory.tool import TextToolMemory
from griptape.engines import VectorQueryEngine
from griptape.drivers import LocalVectorStoreDriver, OpenAiEmbeddingDriver

text_memory = TextToolMemory(
    # Disable all memory activities, so we can use
    # ToolOutputProcessor as a tool later.
    allowlist=[],
    query_engine=VectorQueryEngine(
        vector_store_driver=LocalVectorStoreDriver(
            embedding_driver=OpenAiEmbeddingDriver()
        )
    ),
)

Agent(tool_memory=text_memory, tools=[ToolOutputProcessor()])
```
