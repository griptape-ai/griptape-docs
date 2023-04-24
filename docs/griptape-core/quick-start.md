# Quick Start

To get started, first, install `griptape-core` via `griptape`:

```
pip install griptape -U
```

Next, initialize an executor and some tools:

```python
from griptape.core.adapters import LangchainToolAdapter, ChatgptPluginAdapter
from griptape.core.executors import LocalExecutor
from griptape.tools import (
    Calculator, WebSearch
)

tool_executor = LocalExecutor()

google_search = WebSearch(
    api_search_key="<search key>",
    api_search_id="<search ID>"
)
calculator = Calculator()
```

You can execute tool actions directly:

```python
tool_executor.execute(calculator.calculate, "42**42".encode())
```

Convert tool actions into LangChain tools:

```python
agent = initialize_agent(
    [
        LangchainToolAdapter(executor=tool_executor).generate_tool(google_search.search),
        LangchainToolAdapter(executor=tool_executor).generate_tool(calculator.calculate)
    ],
    OpenAI(temperature=0.5, model_name="text-davinci-003"),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("What is 42^42?")
```

Or generate and run a ChatGPT Plugin:

```python
app = ChatgptPluginAdapter(
    host="localhost:8000",
    path_prefix="/search-tool/",
    executor=tool_executor
).generate_api(google_search)

# run with `uvicorn app:app --reload`
```

Explore more official Griptape tools in the [griptape-tools repo](https://github.com/griptape-ai/griptape-tools).