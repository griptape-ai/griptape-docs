## Overview

You can use Conversation Memory to give Griptape Structures the ability to keep track of the conversation across runs.

!!! Warning
    [Workflows](./workflows.md) do not currently support Conversation Memory.

## Conversation Memory

[ConversationMemory](../../reference/griptape/memory/structure/conversation_memory.md) will keep track of all the tasks input and output.

```python
from griptape.structures import Agent
from griptape.memory.structure import ConversationMemory

Agent(
    memory=ConversationMemory()
)
```

## Buffer Conversation Memory

[BufferConversationMemory](../../reference/griptape/memory/structure/buffer_conversation_memory.md) will keep a sliding window of tasks that are used to construct a prompt:

```python
from griptape.structures import Agent
from griptape.memory.structure import BufferConversationMemory

Agent(
    memory=BufferConversationMemory(buffer_size=3)
)
```

## Summary Conversation Memory

[SummaryConversationMemory](../../reference/griptape/memory/structure/summary_conversation_memory.md) will progressively summarize the whole pipeline except for the last two tasks:

```python
from griptape.structures import Agent
from griptape.memory.structure import SummaryConversationMemory

Agent(
    memory=SummaryConversationMemory(
        offset=2
    )
)
```

## Conversation Memory Drivers

You can persist memory by using Conversation Memory Drivers. Here is how you can initialize memory with a driver:

```python
from griptape.structures import Agent
from griptape.drivers import LocalConversationMemoryDriver
from griptape.memory.structure import ConversationMemory

Agent(
    memory=ConversationMemory(
        driver=LocalConversationMemoryDriver(file_path="memory.json")
    )
)

```

To load memory:

```python
from griptape.drivers import LocalConversationMemoryDriver
from griptape.structures import Agent
from griptape.memory.structure import ConversationMemory

Agent(
    memory=LocalConversationMemoryDriver(file_path="memory.json").load()
)
```

Griptape comes with the following drivers:

- [LocalConversationMemoryDriver](../../reference/griptape/drivers/memory/conversation/local_conversation_memory_driver.md)
- [DynamoDbConversationMemoryDriver](../../reference/griptape/drivers/memory/conversation/dynamodb_conversation_memory_driver.md)

You can build drivers for your own data stores by extending [BaseConversationMemoryDriver](../../reference/griptape/drivers/memory/conversation/base_conversation_memory_driver.md).
