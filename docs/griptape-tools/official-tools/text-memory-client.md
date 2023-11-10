# TextMemoryClient

This tool enables LLMs to query and summarize tool outputs that are stored in short-term tool memory. This tool uniquely requires the user to set the `off_prompt` property explicitly for usability reasons (Griptape doesn't provide the default `True` value).

```python
from griptape.structures import Agent
from griptape.tools import WebScraper, ToolOutputProcessor


Agent(tools=[WebScraper(), ToolOutputProcessor(off_prompt=False)])
```
