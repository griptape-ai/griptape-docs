## Overview

You can use Conversation Memory to give Griptape Structures the ability to keep track of the conversation across runs.

### Agents

[Agents](../structures/agents.md) are created with [ConversationMemory](../../reference/griptape/memory/structure/conversation_memory.md) by default.

```python
from griptape.structures import Agent
from griptape.memory.structure import ConversationMemory

agent = Agent()

agent.run("My favorite animal is a Liger.")
agent.run("What is my favorite animal?")
```

```
[09/19/23 14:21:07] INFO     PromptTask 3e64ca5d5f634a11957cbf46adce251a
                             Input: My favorite animal is a Liger.
[09/19/23 14:21:13] INFO     PromptTask 3e64ca5d5f634a11957cbf46adce251a
                             Output: That's fascinating! Ligers, a hybrid offspring of a male lion and a female tiger, are indeed unique and
                             interesting animals. They are known to be the largest of all big cats. Do you have a particular reason why you
                             like them so much?
                    INFO     PromptTask 3e64ca5d5f634a11957cbf46adce251a
                             Input: What is my favorite animal?
[09/19/23 14:21:15] INFO     PromptTask 3e64ca5d5f634a11957cbf46adce251a
                             Output: Your favorite animal is a Liger, as you previously mentioned.
```

### Pipelines

[Pipelines](../structures/pipelines.md), however, must be explicitly configured with memory.

#### Without Conversation Memory

```python
from griptape.structures import Pipeline
from griptape.tasks import PromptTask

agent = Pipeline()
agent.add_task(
    PromptTask(),
)

agent.run("My favorite food is pizza.")
agent.run("What is my favorite food?")
```

```
[09/19/23 14:43:23] INFO     PromptTask f5ba90e6e877420290574e06f6626e17
                             Input: My favorite food is pizza.
[09/19/23 14:43:27] INFO     PromptTask f5ba90e6e877420290574e06f6626e17
                             Output: That's great! Pizza is a popular favorite for many. There are so many varieties and toppings to choose
                             from. Do you have a specific type or topping that you prefer?
                    INFO     PromptTask f5ba90e6e877420290574e06f6626e17
                             Input: What is my favorite food?
[09/19/23 14:43:33] INFO     PromptTask f5ba90e6e877420290574e06f6626e17
                             Output: As an artificial intelligence, I don't have access to personal data about individuals unless it has been
                             shared with me in the course of our conversation. I'm designed to respect user privacy and confidentiality. So,
                             I'm afraid I don't know what your favorite food is. You're welcome to tell me, though, and I can remember it for
                             our current conversation!
```

#### With Conversation Memory

```python
from griptape.structures import Pipeline
from griptape.tasks import PromptTask
from griptape.memory.structure import ConversationMemory

agent = Pipeline(memory=ConversationMemory())
agent.add_task(
    PromptTask(),
)

agent.run("My favorite food is pizza.")
agent.run("What is my favorite food?")
```

```
[09/19/23 14:42:53] INFO     PromptTask b943a43973274aa59639904ad0483794
                             Input: My favorite food is pizza.
[09/19/23 14:42:56] INFO     PromptTask b943a43973274aa59639904ad0483794
                             Output: That's great! Pizza is a popular favorite for many. There are so many varieties and toppings to choose
                             from. Do you have a specific type or topping that you prefer?
                    INFO     PromptTask b943a43973274aa59639904ad0483794
                             Input: What is my favorite food?
[09/19/23 14:42:58] INFO     PromptTask b943a43973274aa59639904ad0483794
                             Output: Your favorite food is pizza, as you mentioned earlier.
```

### Workflows

!!! Warning
    [Workflows](./workflows.md) do not currently support Conversation Memory.

## Types of Memory

Griptape provides several types of Conversation Memory to fit various use-cases.

### Conversation Memory

[ConversationMemory](../../reference/griptape/memory/structure/conversation_memory.md) will keep track of the full task input and output for all runs.

```python
from griptape.structures import Agent
from griptape.memory.structure import ConversationMemory

agent = Agent(
    memory=ConversationMemory()
)

agent.run("Hello!")

print(agent.memory)
```

You can set the [max_runs](../../reference/memory/structure/conversation_memory.md#griptape.memory.structure.conversation_memory.ConversationMemory.max_runs) parameter to limit how many runs are kept in memory.

```python
from griptape.structures import Agent
from griptape.memory.structure import ConversationMemory

agent = Agent(
    memory=ConversationMemory(max_runs=2)
)

agent.run("Run 1")
agent.run("Run 2")
agent.run("Run 3")
agent.run("Run 4")
agent.run("Run 5")

print(agent.memory.runs[0].input == 'run4')
print(agent.memory.runs[1].input == 'run5')
```

### Summary Conversation Memory

[SummaryConversationMemory](../../reference/griptape/memory/structure/summary_conversation_memory.md) will progressively summarize task input and output of runs.

You can choose to offset which runs are summarized with the
[offset](../../reference/griptape/memory/structure/summary_conversation_memory.md#griptape.memory.structure.summary_conversation_memory.SummaryConversationMemory.offset) parameter.

```python
from griptape.structures import Agent
from griptape.memory.structure import SummaryConversationMemory

agent = Agent(
    memory=SummaryConversationMemory(offset=2)
)

agent.run("Hello!")

print(agent.memory.summary)
```

## Conversation Memory Drivers

You can persist and load memory by using Conversation Memory Drivers. You can build drivers for your own data stores by extending [BaseConversationMemoryDriver](../../reference/griptape/drivers/memory/conversation/base_conversation_memory_driver.md).

```python
from griptape.drivers import LocalConversationMemoryDriver
from griptape.structures import Agent
from griptape.memory.structure import ConversationMemory

memory_driver = LocalConversationMemoryDriver(file_path="memory.json")

agent_1 = Agent(memory=ConversationMemory(driver=memory_driver))
agent_1.run("Skateboarding is my favorite activity.")

agent_2 = Agent(memory=memory_driver.load())
agent_2.run("What is my favorite activity?")
```

### Local Conversation Memory Driver

The [LocalConversationMemoryDriver](../../reference/griptape/drivers/memory/conversation/local_conversation_memory_driver.md) allows you to persist Conversation Memory in a local JSON file.

```python
from griptape.structures import Agent
from griptape.drivers import LocalConversationMemoryDriver
from griptape.memory.structure import ConversationMemory

local_driver = LocalConversationMemoryDriver(file_path="memory.json")
agent = Agent(memory=ConversationMemory(driver=local_driver))

agent.run("Surfing is my favorite sport.")
agent.run("What is my favorite sport?")
```

### DynamoDb Conversation Memory Driver

The [DynamoDbConversationMemoryDriver](../../reference/griptape/drivers/memory/conversation/dynamodb_conversation_memory_driver.md) allows you to persist Conversation Memory in [Amazon DynamoDb](https://aws.amazon.com/dynamodb/).

```python
import os
import uuid
from griptape.drivers import DynamoDbConversationMemoryDriver
from griptape.memory.structure import ConversationMemory
from griptape.structures import Agent

conversation_id = uuid.uuid4().hex
dynamodb_driver = DynamoDbConversationMemoryDriver(
    table_name=os.getenv("DYNAMODB_TABLE_NAME"),
    partition_key="id",
    value_attribute_key="memory",
    partition_key_value=conversation_id,
)

agent = Agent(memory=ConversationMemory(driver=dynamodb_driver))

agent.run("My name is Jeff.")
agent.run("What is my name?")
```

