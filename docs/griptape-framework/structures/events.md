Griptape event listeners can be used to listen for events during a structure's execution.

You can listen to specific event types: 

```python
import logging
from griptape.structures import Agent
from griptape.events import (
    BaseEvent,
    StartTaskEvent,
    FinishTaskEvent,
    StartSubtaskEvent,
    FinishSubtaskEvent,
    StartPromptEvent,
    FinishPromptEvent,
)

def handler(e: BaseEvent):
    logging.getLogger("griptape").info(e)

agent = Agent(
    event_listeners = {
        StartTaskEvent: [handler],
        FinishTaskEvent: [handler],
        StartSubtaskEvent: [handler],
        FinishSubtaskEvent: [handler],
        StartPromptEvent: [handler],
        FinishPromptEvent: [handler],
    }
)

agent.run("tell me about griptape")
```
Or listen to all events:
```python
import logging
from griptape.structures import Agent
from griptape.events import BaseEvent


def handler1(event: BaseEvent):
    logging.getLogger("griptape").info(event)


def handler2(event: BaseEvent):
    logging.getLogger("griptape").info(event)


agent = Agent(event_listeners=[handler1, handler2])

agent.run("tell me about griptape")
```

