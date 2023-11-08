# TextMemoryClient

This tool enables LLMs to query and summarize tool outputs that are stored in short-term tool memory.

```python
from griptape.structures import Agent
from griptape.tools import WebScraper, ToolOutputProcessor


Agent(tools=[WebScraper(), ToolOutputProcessor(off_prompt=False)])
```
