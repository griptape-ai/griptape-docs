## Overview

Conversation memory can be used to give Griptape structures memory of the conversation.

!!! Warning
    [Workflows](./workflows.md) do not currently support conversation memory.

## ConversationMemory

By default, Griptape structures don't initialize memory, so you have to explicitly pass it to them:

```python
from griptape.structures import Agent
from griptape.memory.structure import ConversationMemory

Agent(
    memory=ConversationMemory()
)
```

## BufferConversationMemory

`BufferConversationMemory` will keep a sliding window of tasks that are used to construct a prompt:

```python
from griptape.structures import Agent
from griptape.memory.structure import BufferConversationMemory

Agent(
    memory=BufferConversationMemory(buffer_size=3)
)
```

## SummaryConversationMemory

`SummaryConversationMemory` will progressively summarize the whole pipeline except for the last two tasks:

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

You can persist memory by using memory drivers. Here is how you can initialize memory with a driver:

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

You can build drivers for your own data stores by extending [BaseConversationMemoryDriver](../../reference/griptape/drivers/memory/conversation/dynamodb_conversation_memory_driver.md).
