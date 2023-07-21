# ToolOutputProcessor

This tool enables LLMs to query, extract, and summarize tool outputs via shared short-term tool memory. Before using it, you'll likely want to disable all memory activities, so the LLM doesn't get confused which one to use. THis tool is helpful when you want the queried memory output to go back to memory.

```python
text_memory = TextToolMemory(
    allowlist=[]
)

agent = Agent(
    tool_memory=text_memory,
    tools=[ToolOutputProcessor()]
)
```