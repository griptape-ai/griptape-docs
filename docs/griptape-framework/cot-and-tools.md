# Chains of Thought and Tools

The most powerful feature of **griptape** is the ability of workflow tasks to generate *chains of thought* (CoT) and use tools that can interact with the outside world. We use the [ReAct](https://arxiv.org/abs/2210.03629) technique to implement CoT reasoning and acting in the underlying LLMs without using any fine-tuning.

**griptape** implements the reasoning loop in the `ToolkitTask` and integrates griptape-tools natively.

Here is an example on how to use tools:

```python
from griptape.tools import WebScraper, Calculator
from griptape.drivers import OpenAiPromptDriver
from griptape.memory import Memory
from griptape.tasks import PromptTask, ToolkitTask
from griptape.structures import Pipeline
from griptape.core import ToolLoader


scraper = WebScraper()
calculator = Calculator()

pipeline = Pipeline(
    memory=Memory(),
    prompt_driver=OpenAiPromptDriver(
        model="gpt-4"
    ),
    tool_loader=ToolLoader(
        tools=[calculator, scraper]
    )
)

pipeline.add_tasks(
    ToolkitTask(
        tool_names=[calculator.name, scraper.name]
    )
)

pipeline.run("what's 5^23?")
```