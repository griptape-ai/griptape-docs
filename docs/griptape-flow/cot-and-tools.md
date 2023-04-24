# Chains of Thought and Tools

The most powerful feature of griptape-flow is the ability of workflow steps to generate *chains of thought* (CoT) and use tools that can interact with the outside world. We use the [ReAct](https://arxiv.org/abs/2210.03629) technique to implement CoT reasoning and acting in the underlying LLMs without using any fine-tuning.

griptape-flow implements the reasoning loop in the `ToolkitStep` and integrates [Griptape](../../griptape_core/) tools natively.

Here is an example on how to use tools:

```python
from decouple import config
from griptape.tools import WebScraper, Calculator
from griptape.flow import utils
from griptape.flow.drivers import OpenAiPromptDriver
from griptape.flow.memory import PipelineMemory
from griptape.flow.steps import PromptStep, ToolkitStep
from griptape.flow.structures import Pipeline
from griptape.flow.utils import ToolLoader


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
    )
)

pipeline.run("what's 5^23?")
```