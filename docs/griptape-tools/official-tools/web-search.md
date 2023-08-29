# WebSearch

This tool enables LLMs to search the web.

```python
import os
from griptape.tools import WebSearch

WebSearch(
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    google_api_search_id=os.environ.get("GOOGLE_API_SEARCH_ID")
)
```
