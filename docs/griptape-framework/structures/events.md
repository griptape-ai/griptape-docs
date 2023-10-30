## Overview

Griptape Event Listeners can be used to listen for events during a structure's execution.

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

## Streaming


You can use the [CompletionChunkEvent](../../reference/griptape/events/completion_chunk_event.md) to stream the completion results from Prompt Drivers.

```python
from griptape.events import CompletionChunkEvent
from griptape.tasks import ToolkitTask
from griptape.structures import Pipeline
from griptape.tools import WebScraper


pipeline = Pipeline(
    event_listeners={
        CompletionChunkEvent: [
            lambda e: print(e.token, end="", flush=True),
        ],
    },
)

pipeline.add_tasks(
    ToolkitTask(
        "Based on https://griptape.ai, tell me what griptape is.",
        tools=[WebScraper()],
    ),
)

pipeline.run()
```

You can also use the [Stream](../../reference/griptape/utils/stream.md) utility to automatically wrap
[CompletionChunkEvent](../../reference/griptape/events/completion_chunk_event.md)s in a Python iterator.

```python
from griptape.utils import Stream
from griptape.tasks import ToolkitTask
from griptape.structures import Pipeline
from griptape.tools import WebScraper


pipeline = Pipeline()
pipeline.add_tasks(
    ToolkitTask(
        "Based on https://griptape.ai, tell me what griptape is.",
        tools=[WebScraper()],
    ),
)

for artifact in Stream(pipeline).run():
    print(artifact.value, end="", flush=True),
```


## Counting Tokens

To count tokens you can use Event Listeners and the [TokenCounter](../../reference/griptape/utils/token_counter.md) util:

```python
from griptape import utils
from griptape.events import StartPromptEvent, FinishPromptEvent, EventListener
from griptape.structures import Agent


token_counter = utils.TokenCounter()

agent = Agent(
    event_listeners=[
        EventListener(
            lambda e: token_counter.add_tokens(e.token_count),
            event_types=[StartPromptEvent, FinishPromptEvent],
        ),
    ]
)

agent.run("tell me about large language models")

print(f"total tokens: {token_counter.tokens}")
```

```
[09/25/23 16:32:41] INFO     PromptTask c93569eb1d264675b52bef184b269621
                             Input: tell me about large language models
[09/25/23 16:33:01] INFO     PromptTask c93569eb1d264675b52bef184b269621
                             Output: Large language models are a type of artificial intelligence model that are trained on
                             a vast amount of text data. They are designed to generate human-like text based on the input
                             they are given. These models can answer questions, write essays, summarize texts, translate
                             languages, and even generate creative content like poetry or stories.

                             One of the most well-known large language models is GPT-3, developed by OpenAI. It has 175
                             billion machine learning parameters and was trained on hundreds of gigabytes of text.

                             These models work by predicting the probability of a word given the previous words used in
                             the text. They don't understand text in the way humans do, but they can generate coherent and
                             contextually relevant sentences by learning patterns in the data they were trained on.

                             However, they also have limitations. For instance, they can sometimes generate incorrect or
                             nonsensical responses. They can also be sensitive to slight changes in input phrasing, and
                             they don't have the ability to fact-check information or access real-time data, so they can't
                             provide up-to-date information or verify the truthfulness of their outputs. They also don't
                             have a sense of ethics or morality, so they rely on guidelines and safety measures put in
                             place by their developers.
total tokens: 273
```
