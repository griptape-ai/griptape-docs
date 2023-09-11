## Overview

Prompt Drivers are used by Griptape Structures to make API calls to the underlying LLMs. [OpenAiChatPromptDriver](../../reference/griptape/drivers/prompt/openai_chat_prompt_driver.md) is the default prompt driver used in all structures.

You can instantiate drivers and pass them to structures:

```python
from griptape.structures import Pipeline
from griptape.drivers import OpenAiChatPromptDriver

Pipeline(
    prompt_driver=OpenAiChatPromptDriver(
        temperature=0.3
    )
)
```

Or use them independently:

```python
from griptape.utils import PromptStack
from griptape.drivers import OpenAiChatPromptDriver

stack = PromptStack()

stack.add_user_input("What's the word, bird?")

OpenAiChatPromptDriver(
    temperature=1
).run(stack)
```

## OpenAI Chat

The [OpenAiChatPromptDriver](../../reference/griptape/drivers/prompt/openai_chat_prompt_driver.md) connects to the [OpenAI Chat](https://platform.openai.com/docs/guides/chat) API.

## OpenAI Completion

The [OpenAiCompletionPromptDriver](../../reference/griptape/drivers/prompt/openai_completion_prompt_driver.md) connects to the [OpenAI Completion](https://platform.openai.com/docs/guides/completion) API.

## Azure OpenAI

The [AzureOpenAiPromptDriver](../../reference/griptape/drivers/prompt/azure_openai_completion_prompt_driver.md) connects to Azure OpenAI [Text Completion](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/reference) and [Chat Completion](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/reference) APIs.

## Cohere

The [CoherePromptDriver](../../reference/griptape/drivers/prompt/cohere_prompt_driver.md) connects to the Cohere [Generate](https://docs.cohere.ai/reference/generate) API.

## Anthropic

The [AnthropicPromptDriver](../../reference/griptape/drivers/prompt/anthropic_prompt_driver.md) connects to the Anthropic [Completions](https://docs.anthropic.com/claude/reference/complete_post) API.

## Hugging Face Hub

The [HuggingFaceHubPromptDriver](../../reference/griptape/drivers/prompt/hugging_face_hub_prompt_driver.md) connects to the [Hugging Face API](https://huggingface.co/docs/hub/api). It supports models with the following tasks:

* text2text-generation
* text-generation

## Hugging Face Pipeline

The [HuggingFaceHubPromptDriver](../../reference/griptape/drivers/prompt/hugging_face_pipeline_prompt_driver.md) uses [Hugging Face Pipelines](https://huggingface.co/docs/transformers/main_classes/pipelines) for inference locally. It supports models with the following tasks:

* text2text-generation
* text-generation
