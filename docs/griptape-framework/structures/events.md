## Overview

Griptape Event Listeners can be used to listen for events during a structure's execution. This can be useful when [counting tokens](../../examples/count-tokens.md) being sent to the LLM.

## Specific Event Types

You can listen to specific event types:

```python
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

def handler(event: BaseEvent):
    print(event.__class__)

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
```
<class 'griptape.events.start_task_event.StartTaskEvent'>
[09/08/23 10:51:16] INFO     PromptTask a20c236d1d86480fb14ae976e6cf8983
                             Input: tell me about griptape
<class 'griptape.events.start_prompt_event.StartPromptEvent'>
<class 'griptape.events.finish_prompt_event.FinishPromptEvent'>
[09/08/23 10:51:27] INFO     PromptTask a20c236d1d86480fb14ae976e6cf8983
                             Output: Griptape is a gritty, sandpaper-like material that is applied to the top of a skateboard deck. It
                             provides traction and grip, allowing skateboarders to keep their feet firmly on the board and perform tricks more
                             easily. Griptape comes in different colors and designs, but the most common type is black. It's adhesive on one
                             side so it can stick to the skateboard. Over time, griptape can wear down and need to be replaced to maintain
                             optimal performance. It's an essential component for skateboarding and other similar sports.
<class 'griptape.events.finish_task_event.FinishTaskEvent'>
```

## All Event Types

Or listen to all events with multiple handlers:

```python
from griptape.structures import Agent
from griptape.events import BaseEvent


def handler1(event: BaseEvent):
    print("Handler 1", event.__class__)


def handler2(event: BaseEvent):
    print("Handler 2", event.__class__)


agent = Agent(event_listeners=[handler1, handler2])

agent.run("tell me about griptape")
```

```
Handler 1 <class 'griptape.events.start_task_event.StartTaskEvent'>
Handler 2 <class 'griptape.events.start_task_event.StartTaskEvent'>
[09/08/23 10:52:36] INFO     PromptTask cba4944d74f34b43990d7dc6f7ffe0d1
                             Input: tell me about griptape
Handler 1 <class 'griptape.events.start_prompt_event.StartPromptEvent'>
Handler 2 <class 'griptape.events.start_prompt_event.StartPromptEvent'>
Handler 1 <class 'griptape.events.finish_prompt_event.FinishPromptEvent'>
Handler 2 <class 'griptape.events.finish_prompt_event.FinishPromptEvent'>
[09/08/23 10:52:54] INFO     PromptTask cba4944d74f34b43990d7dc6f7ffe0d1
                             Output: Griptape is a gritty, sandpaper-like material that is applied to the top of a skateboard deck. It
                             provides traction between the skateboarder's shoes and the board itself, allowing for better control and
                             stability when performing tricks and maneuvers.

                             Griptape comes in a variety of colors and designs, but the most common type is black. It's typically made from a
                             sheet of paper or fabric with an adhesive back and a layer of crushed silicon carbide or aluminum oxide on the
                             top.

                             To apply griptape, you peel off the backing, stick it to your board, and then cut off the excess. It's important
                             to replace your griptape regularly to ensure it maintains its grip. Over time, it can become less effective due
                             to wear and tear.

                             In addition to skateboarding, griptape is also used in other board sports such as longboarding and snowboarding.
Handler 1 <class 'griptape.events.finish_task_event.FinishTaskEvent'>
Handler 2 <class 'griptape.events.finish_task_event.FinishTaskEvent'>
```
