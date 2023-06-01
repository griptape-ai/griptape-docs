# Agents

Agents are similar to pipelines, but they only consist of one task.

Tasks in the workflow have access to the following `context` variables:

* `args`: arguments passed to the `Construct.run()` method.
* `structure`: the structure that the task belongs to.

Using agents is similar to pipelines:

```python
from griptape.tools import Calculator
from griptape.memory.structure import ConversationMemory
from griptape.tasks import ToolkitTask
from griptape.structures import Agent

calculator = Calculator()

agent = Agent(
    task=ToolkitTask(
        tools=[calculator]
    ),
)

agent.run("what's 123^312?")
```
