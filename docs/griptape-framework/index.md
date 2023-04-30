**griptape** is a modular Python framework for LLM workflows, tools, memory, and data that enables developers to:

1. 🤖 Build **AI agents**, sequential **LLM pipelines** and sprawling **DAG workflows** for complex use cases.
2. ⛓️ Augment LLMs with **chain of thought** capabilities.
3. 🧰️ Integrate other services and functionality into LLMs as [tools](https://github.com/griptape-ai/griptape-tools) (e.g., calculators, web scrapers, spreadsheet editors, and API connectors); run tools in any environment (local, containerized, cloud, etc.); use tools directly in **griptape** or convert them into middleware abstractions, such as ChatGPT Plugins, LangChain tools, or Fixie.ai agents.
4. 💾 Add **memory** to AI pipelines for context preservation and summarization.

## Quick Start

First, install **griptape** and **griptape-tools**:

```
pip install griptape griptape-tools -U
```

Second, configure an OpenAI client by [getting an API key](https://beta.openai.com/account/api-keys) and adding it to your environment as `OPENAI_API_KEY`. **griptape** uses [OpenAI Completions API](https://platform.openai.com/docs/guides/completion) to execute LLM prompts and to work with [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html) data structures.

### Building a Pipeline

With **griptape**, you can create *structures*, such as `Pipelines` and `Workflows`, that are composed of different types of tasks. You can also define structures as JSON objects and load them into **griptape** dynamically. Let's define a simple two-task pipeline that uses tools:

```python
from decouple import config
from griptape.tools import WebScraper
from griptape import utils
from griptape.drivers import OpenAiPromptDriver
from griptape.memory import Memory
from griptape.tasks import PromptTask, ToolkitTask
from griptape.structures import Pipeline
from griptape.core import ToolLoader


scraper = WebScraper(
    openai_api_key=config("OPENAI_API_KEY")
)

pipeline = Pipeline(
    memory=Memory(),
    prompt_driver=OpenAiPromptDriver(
        model="gpt-4"
    ),
    tool_loader=ToolLoader(
        tools=[scraper]
    )
)

pipeline.add_tasks(
    ToolkitTask(
        tool_names=[scraper.name]
    ),
    PromptTask(
        "Say the following like a pirate: {{ input }}"
    )
)

pipeline.run("Give me a summary of https://en.wikipedia.org/wiki/Large_language_model")

print(utils.Conversation(pipeline.memory).to_string())
```

Boom! Our first conversation, à la ChatGPT, is here:

> Q: Give me a summary of https://en.wikipedia.org/wiki/Large_language_model  
> A: Arr, me hearties! Large language models have been developed and set sail since 2018, includin' BERT, GPT-2, GPT-3 [...]

### Using Tools

First, initialize an executor and some tools:

```python
from griptape.converters import LangchainToolConverter, ChatgptPluginConverter
from griptape.executors import LocalExecutor
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

You can execute tool activities directly:

```python
tool_executor.execute(calculator.calculate, "42**42".encode())
```

Convert tool activities into LangChain tools:

```python
agent = initialize_agent(
    [
        LangchainToolConverter(executor=tool_executor).generate_tool(google_search.search),
        LangchainToolConverter(executor=tool_executor).generate_tool(calculator.calculate)
    ],
    OpenAI(temperature=0.5, model_name="text-davinci-003"),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("What is 42^42?")
```

Or generate and run a ChatGPT Plugin:

```python
app = ChatgptPluginConverter(
    host="localhost:8000",
    path_prefix="/search-tool/",
    executor=tool_executor
).generate_api(google_search)

# run with `uvicorn app:app --reload`
```

Explore more official Griptape tools in the [griptape-tools repo](https://github.com/griptape-ai/griptape-tools).