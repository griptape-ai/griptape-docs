# WebSearch

This tool enables LLMs to search the web.

```python
from griptape.tools import WebSearch
from griptape.structures import Agent

# Initialize the WebSearch tool with necessary parameters
web_search_tool = WebSearch(
    results_count=5,
    google_api_lang="lang_en",
    google_api_key="YOUR_GOOGLE_API_KEY_HERE",
    google_api_search_id="YOUR_GOOGLE_SEARCH_ENGINE_ID_HERE",
    google_api_country="us"
)

# Set up an agent using the WebSearch tool
agent = Agent(
    tools=[web_search_tool]
)

# Task: Search the web for a specific query
search_result = agent.run({
    "description": "Search the web for a query",
    "tool": "WebSearch",
    "activity": "search",
    "values": {
        "query": "How does photosynthesis work?"
    }
})

print(f"Search Result: {search_result}")
```
