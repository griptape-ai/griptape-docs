The most powerful feature of Griptape is the ability of workflow tasks to generate *chains of thought* (CoT) and use tools that can interact with the outside world. We use the [ReAct](https://arxiv.org/abs/2210.03629) technique to implement CoT reasoning and acting in the underlying LLMs without using any fine-tuning.

Griptape implements the reasoning loop in the `ToolkitTask` and integrates griptape-tools natively.

Here is an example on how to use tools:

```python
from griptape.tools import WebScraper, Calculator
from griptape.memory.structure import ConversationMemory
from griptape.tasks import PromptTask, ToolkitTask
from griptape.structures import Pipeline


scraper = WebScraper()
calculator = Calculator()

pipeline = Pipeline(
    memory=ConversationMemory()
)

pipeline.add_tasks(
    ToolkitTask(
        tools=[calculator, scraper]
    )
)

pipeline.run("what's 5^23?")
```