Griptape is a modular Python framework for LLM workflows, tools, memory, and data that enables developers to:

1. 🤖 Build **AI agents**, sequential **LLM pipelines** and sprawling **DAG workflows** for complex use cases.
2. ⛓️ Augment LLMs with **chain of thought** capabilities.
3. 🧰️ Integrate other services and functionality into LLMs as [tools](https://github.com/griptape-ai/griptape-tools) (e.g., calculators, web scrapers, spreadsheet editors, and API connectors); run tools in any environment (local, containerized, cloud, etc.); and wrap tools with off prompt data storage that prevents LLMs from accessing your data directly.
4. 💾 Add **memory** to AI pipelines for context preservation and summarization.

## Quick Start

First, configure an OpenAI client by [getting an API key](https://beta.openai.com/account/api-keys) and adding it to your environment as `OPENAI_API_KEY`. Griptape uses [OpenAI Completions API](https://platform.openai.com/docs/guides/completion) to execute LLM prompts and to work with [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html) data structures.

### Using pip

Install **griptape** and **griptape-tools**:

```
pip install griptape griptape-tools -U
```

### Using Poetry

To get started with Griptape using Poetry first create a new poetry project from the terminal: 

```
% poetry new griptape-quickstart
Created package griptape_quickstart in griptape-quickstart
```

If you're using PyCharm, open the directory, and you'll be prompted to setup the Poetry environment.:

![Poetry Setup](../assets/tools/poetry_setup.png)

Add `griptape = "*"` to your **pyproject.yml** file. You should notice PyCharm asking if it should run `poetry update`. The answer is yes:

![TOML](../assets/tools/toml.png)

### Build a Simple Pipeline

With Griptape, you can create *structures*, such as `Agents`, `Pipelines`, and `Workflows`, that are composed of different types of tasks. Let's define a simple two-task pipeline that uses tools and ramps:

```python
from griptape.memory import Memory
from griptape.ramps import TextStorageRamp, BlobStorageRamp
from griptape.structures import Pipeline
from griptape.tasks import ToolkitTask, PromptTask
from griptape.tools import WebScraper, TextProcessor, FileManager
from griptape import utils


# Ramps enable LLMs to store and manipulate data without ever looking at it directly.
text_storage = TextStorageRamp()
blob_storage = BlobStorageRamp()

# Connect a web scraper to load web pages.
web_scraper = WebScraper(
    ramps={
        "get_content": [text_storage]
    }
)

# TextProcessor enables LLMs to summarize and query text.
text_processor = TextProcessor(
    ramps={
        "summarize": [text_storage],
        "query": [text_storage]
    }
)

# File manager can load and store files locally.
file_manager = FileManager(
    ramps={
        "load": [blob_storage],
        "save": [text_storage, blob_storage]
    }
)

# Pipelines represent sequences of tasks.
pipeline = Pipeline(
    memory=Memory()
)

pipeline.add_tasks(
    # Load up the first argument from `pipeline.run`.
    ToolkitTask(
        "{{ args[0] }}",
        tools=[web_scraper, text_processor, file_manager]
    ),
    # Augment `input` from the previous task.
    PromptTask(
        "Say the following in spanish: {{ input }}"
    )
)

result = pipeline.run("Load https://griptape.readthedocs.io, summarize it, and store it in griptape.txt")

print(utils.Conversation(pipeline.memory))
```

Boom! Our first LLM pipeline with two sequential tasks generated the following exchange:

> Q: Load https://griptape.readthedocs.io, summarize it, and store it in griptape.txt  
> A: El contenido de https://griptape.readthedocs.io ha sido resumido y almacenado en griptape.txt.