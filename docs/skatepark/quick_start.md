# Quick Start

First, install Skatepark, Griptape Tools, and Decouple:

```
pip install skatepark-lib griptape-tools python-decouple
```

Second, configure an OpenAI client by [getting an API key](https://beta.openai.com/account/api-keys) and adding it to your environment as `OPENAI_API_KEY`. Skatepark uses [OpenAI Completions API](https://platform.openai.com/docs/guides/completion) to execute LLM prompts and to work with [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/index.html) data structures.

With Skatepark, you can create *structures*, such as `Pipelines` and `Workflows`, that are composed of different types of steps. You can also define structures as JSON objects and load them into Skatepark dynamically. Let's define a simple two-step pipeline that uses tools:

```python
from decouple import config
from griptape.tools import WebScraper, Calculator
from skatepark import utils
from skatepark.drivers import OpenAiPromptDriver
from skatepark.memory import PipelineMemory
from skatepark.steps import PromptStep, ToolkitStep
from skatepark.structures import Pipeline
from skatepark.utils import ToolLoader


scraper = WebScraper(
    openai_api_key=config("OPENAI_API_KEY")
)
calculator = Calculator()

pipeline = Pipeline(
    memory=PipelineMemory(),
    prompt_driver=OpenAiPromptDriver(
        model="gpt-4"
    ),
    tool_loader=ToolLoader(
        tools=[calculator, scraper]
    )
)

pipeline.add_steps(
    ToolkitStep(
        tool_names=[calculator.name, scraper.name]
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