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
from griptape.ramps import StorageRamp
from griptape.tasks import PromptTask, ToolkitTask
from griptape.structures import Agent
from griptape.core import ToolLoader

storage = StorageRamp(
    driver=MemoryStorageDriver()
)

scraper = WebScraper(
    ramps={
        "get_content": [storage]
    }
)

agent = Agent(
    task=ToolkitTask(
        tool_names=[scraper.name]
    ),
    memory=Memory(),
    # remove prompt_driver if you don't have access to gpt-4.
    # it'll default to 3.5-turbo
    prompt_driver=OpenAiPromptDriver(
        model="gpt-4"
    ),
    tool_loader=ToolLoader(
        tools=[scraper]
    )
)

agent.run("Give me a summary of https://en.wikipedia.org/wiki/Large_language_model")
```
