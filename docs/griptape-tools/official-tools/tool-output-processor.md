# ToolOutputProcessor

This tool enables LLMs to query, extract, and summarize tool outputs via shared short-term tool memory. Before using it, you'll likely want to disable all memory activities, so the LLM doesn't get confused which one to use. THis tool is helpful when you want the queried memory output to go back to memory.

```python
from griptape.tools import ToolOutputProcessor
from griptape.structures import Agent
from griptape.memory.tool import TextToolMemory

# Set up memories
mem1 = TextToolMemory(name="memory_1")

# Initialize the ToolOutputProcessor
tool_processor = ToolOutputProcessor(
    input_memory=[mem1],
    top_n=5
)

# Set up an agent using the ToolOutputProcessor tool
agent = Agent(
    tools=[tool_processor]
)

# First, insert some text into the memory so that we have something to search.
agent.run({
    "description": "Insert text",
    "tool": "ToolOutputProcessor",
    "activity": "insert",
    "values": {
        "memory_name": "memory_1",
        "artifact_namespace": "namespace_1",
        "text": "This is an example text about griptape."
    }
})

# Task: Search memory content
search_result = agent.run({
    "description": "Search memory",
    "tool": "ToolOutputProcessor",
    "activity": "search",
    "values": {
        "memory_name": "memory_1",
        "artifact_namespace": "namespace_1",
        "query": "What is griptape?"
    }
})

print(f"Search Result: {search_result}")
```
