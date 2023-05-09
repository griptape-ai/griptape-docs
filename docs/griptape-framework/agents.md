# Agents

Agents are similar to pipelines, but they only consist of one task.

Tasks in the workflow have access to the following `context` variables:

- `args`: arguments passed to the `Construct.run()` method.
- `structure`: the structure that the task belongs to.

Using agents is similar to pipelines:

```python
from griptape.tools import WebScraper
from griptape.drivers import OpenAiPromptDriver
from griptape.memory import Memory
from griptape.tasks import PromptTask, ToolkitTask
from griptape.structures import Agent
from griptape.core import ToolLoader

scraper = WebScraper()

agent = Agent(
    task=ToolkitTask(
        tool_names=[scraper.name]
    ),
    memory=Memory(),
    prompt_driver=OpenAiPromptDriver(
        model="gpt-4"
    ),
    tool_loader=ToolLoader(
        tools=[scraper]
    )
)

agent.run("Give me a summary of https://en.wikipedia.org/wiki/Large_language_model")
```