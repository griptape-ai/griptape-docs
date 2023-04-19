# Quick Start

First, install griptape:

```
pip install griptape
```

Second, configure an OpenAI client by [getting an API key](https://beta.openai.com/account/api-keys) and adding it to your environment as `OPENAI_API_KEY`. griptape-flow uses [OpenAI Completions API](https://platform.openai.com/docs/guides/completion) to execute LLM prompts and to work with [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html) data structures.

With griptape-flow, you can create *structures*, such as `Pipelines` and `Workflows`, that are composed of different types of steps. You can also define structures as JSON objects and load them into griptape-flow dynamically. Let's define a simple two-step pipeline that uses tools:

```python
from decouple import config
from griptape.tools import WebScraper
from griptape.flow import utils
from griptape.flow.drivers import OpenAiPromptDriver
from griptape.flow.memory import PipelineMemory
from griptape.flow.steps import PromptStep, ToolkitStep
from griptape.flow.structures import Pipeline
from griptape.flow.utils import ToolLoader


scraper = WebScraper(
    openai_api_key=config("OPENAI_API_KEY")
)

pipeline = Pipeline(
    memory=PipelineMemory(),
    prompt_driver=OpenAiPromptDriver(
        model="gpt-4"
    ),
    tool_loader=ToolLoader(
        tools=[scraper]
    )
)

pipeline.add_steps(
    ToolkitStep(
        tool_names=[scraper.name]
    ),
    PromptStep(
        "Say the following like a pirate: {{ input }}"
    )
)

pipeline.run("Give me a summary of https://en.wikipedia.org/wiki/Large_language_model")

print(utils.Conversation(pipeline.memory).to_string())

```

Boom! Our first conversation, à la ChatGPT, is here:

> Q: Give me a summary of https://en.wikipedia.org/wiki/Large_language_model  
> A: Arr, me hearties! Large language models have been developed and set sail since 2018, includin' BERT, GPT-2, GPT-3 [...]