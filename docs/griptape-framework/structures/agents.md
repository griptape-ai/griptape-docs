## Overview

An [Agent](../../reference/griptape/structures/agent.md) is the quickest way to get started with Griptape.
Agents take in [tools](../../reference/griptape/structures/agent.md#griptape.structures.agent.Agent.tools) and [input_template](../../reference/griptape/structures/agent.md#griptape.structures.agent.Agent.input_template)
directly, which the agent uses to dynamically determine whether to use a [Prompt Task](./tasks.md#prompt-task) or [Toolkit Task](./tasks.md#toolkit-task).

If [tools](../../reference/griptape/structures/agent.md#griptape.structures.agent.Agent.tools) are passed provided to the Agent, a [Toolkit Task](./tasks.md#toolkit-task) will be used. If no [tools](../../reference/griptape/structures/agent.md#griptape.structures.agent.Agent.tools)
are provided, a [Prompt Task](./tasks.md#prompt-task) will be used.

## Toolkit Task Agent

```python
from griptape.tools import Calculator
from griptape.structures import Agent


agent = Agent(
    input_template="Calculate the following: {{ args[0] }}",
    tools=[Calculator(off_prompt=False)]
)

agent.run("what's 123^5?")
```

```
[03/28/24 09:38:24] INFO     ToolkitTask 1420d56d67084cb5829ea0510f0f0712
                             Input: Calculate the following: what's 123^5?
[03/28/24 09:38:29] INFO     Subtask 41d8edfda21a4bf884fc9c0a40a98b2e
                             Thought: The user wants to calculate the value of 123 raised to the power of 5. I will use the Calculator action to perform this calculation.
                             Actions: [
                               {
                                 "name": "Calculator",
                                 "path": "calculate",
                                 "input": {
                                   "values": {
                                     "expression": "123**5"
                                   }
                                 },
                                 "output_label": "calculation_result"
                               }
                             ]
                    INFO     Subtask 41d8edfda21a4bf884fc9c0a40a98b2e
                             Response: calculation_result output: 28153056843
[03/28/24 09:38:31] INFO     ToolkitTask 1420d56d67084cb5829ea0510f0f0712
                             Output: The result of 123 raised to the power of 5 is 28153056843.
```

## Prompt Task Agent

```python
from griptape.structures import Agent
from griptape.tasks import PromptTask


agent = Agent()
agent.add_task(
    PromptTask(
        "Write me a {{ creative_medium }} about {{ args[0] }} and {{ args[1] }}",
        context={
            'creative_medium': 'haiku'
        }
    )
)

agent.run("Skateboards", "Programming")
```

```
[09/08/23 10:10:24] INFO     PromptTask e70fb08090b24b91a9307fa83479e851
                             Input: Write me a haiku about Skateboards and Programming
[09/08/23 10:10:28] INFO     PromptTask e70fb08090b24b91a9307fa83479e851
                             Output: Code on wheels in flight,
                             Skateboards meet algorithms bright,
                             In binary, we ignite.
```
