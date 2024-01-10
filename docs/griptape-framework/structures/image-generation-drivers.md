## Overview

Image generation Drivers are used by [image generation Engines](../data/image-generation-engines.md) to build and execute API calls to image generation models.

Provide a Driver when building an [Engine](../data/image-generation-engines.md), then pass it to a [Tool](../tools/index.md) for use by an [Agent](../structures/agents.md):

```python
from griptape.structures import Agent
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import OpenAiDalleImageGenerationDriver
from griptape.tools import PromptImageGenerationClient, FileManager

driver = OpenAiDalleImageGenerationDriver(
    model="dall-e-3",
)

engine = PromptImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    PromptImageGenerationClient(engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

### Amazon Bedrock

The Amazon Bedrock Driver provides multi-model access to image generation models hosted by Amazon Bedrock. This Driver manages the API calls to the Bedrock API, while the specific Model Drivers below format the API requests and parse the responses.

#### Bedrock Stable Diffusion Model Driver

The Bedrock Stable Diffusion Model Driver provides support for Stable Diffusion models hosted by Amazon Bedrock. This Model Driver supports configurations specific to Stable Diffusion, like style presets, clip guidance presets, and sampler.

This Model Driver supports negative prompts. When provided (for example, when used with an [image generation Engine](../data/image-generation-engines.md) configured with [Negative Rulesets](../data/image-generation-engines.md#image-generation-engine-rulesets)), the image generation request will include negatively-weighted prompts describing features or characteristics to avoid in the resulting generation.

```python
from griptape.structures import Agent
from griptape.tools import PromptImageGenerationClient, FileManager
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver

model_driver = BedrockStableDiffusionImageGenerationModelDriver(
    style_preset="pixel-art",
    steps=50,
)

driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=model_driver,
    model="stability.stable-diffusion-xl-v0",
)

engine = PromptImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    PromptImageGenerationClient(engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

#### Amazon Bedrock Titan Image Generator Model Driver

The Amazon Bedrock Titan Image Generator Model Driver provides support for Titan Image Generator models hosted by Amazon Bedrock. This Model Driver supports configurations specific to Titan Image Generator, like quality, seed, and cfg_scale.

This Model Driver supports negative prompts. When provided (for example, when used with an [image generation engine](../data/image-generation-engines.md) configured with [Negative Rulesets](../data/image-generation-engines.md#image-generation-engine-rulesets)), the image generation request will include negatively-weighted prompts describing features or characteristics to avoid in the resulting generation.

```python
from griptape.structures import Agent
from griptape.tools import PromptImageGenerationClient, FileManager
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockTitanImageGenerationModelDriver

model_driver = BedrockTitanImageGenerationModelDriver(
    quality="hd",
)

driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=model_driver,
    model="stability.stable-diffusion-xl-v0",
)

engine = PromptImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    PromptImageGenerationClient(engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

### Azure OpenAI DALL-E

The Azure OpenAI DALL-E image generation Driver provides access to OpenAI DALL-E models hosted by Azure. In addition to the configurations provided by the underlying OpenAI DALL-E Driver, the Azure OpenAI Dall-E Driver allows configuration of Azure-specific deployment values.

```python
from griptape.structures import Agent
from griptape.tools import PromptImageGenerationClient, FileManager
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import AzureOpenAiDalleImageGenerationDriver

driver = AzureOpenAiDalleImageGenerationDriver(
    model="dall-e-3",
    azure_deployment="my-azure-deployment",
    azure_endpoint="https://example-endpoint.openai.azure.com",
)

engine = PromptImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    PromptImageGenerationClient(engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

### Leonardo.Ai

The Leonardo image generation Driver enables image generation using models hosted by [Leonardo.ai](https://leonardo.ai/).

This Driver supports configurations like model selection, image size, specifying a generation seed, and generation steps. For details on supported configuration parameters, see [Leonardo.Ai's image generation documentation](https://docs.leonardo.ai/reference/creategeneration).

This Driver supports negative prompts. When provided (for example, when used with an [image generation engine](../data/image-generation-engines.md) configured with [Negative Rulesets](../data/image-generation-engines.md#image-generation-engine-rulesets)), the image generation request will include negatively-weighted prompts describing features or characteristics to avoid in the resulting generation.

```python
import os

from griptape.structures import Agent
from griptape.tools import PromptImageGenerationClient, FileManager
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import LeonardoImageGenerationDriver

driver = LeonardoImageGenerationDriver(
    model="6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",
    api_key=os.getenv("LEONARDO_API_KEY"),
    image_width=512,
    image_height=1024,
)

engine = PromptImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    PromptImageGenerationClient(engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

### OpenAI DALL-E

The OpenAI DALL-E image generation Driver enables image generation using OpenAI DALL-E models. Like other OpenAI Drivers, the image generation Driver will implicitly load an API key in the `OPENAI_API_KEY` environment variable if one is not explicitly provided.

The OpenAI Dall-E Driver supports image generation configurations like style presets, image quality preference, and image size. For details on supported configuration values, see the [OpenAI documentation](https://platform.openai.com/docs/guides/images/introduction).

```python
from griptape.structures import Agent
from griptape.tools import PromptImageGenerationClient, FileManager
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import OpenAiDalleImageGenerationDriver

driver = OpenAiDalleImageGenerationDriver(
    model="dall-e-2",
    image_size="512x512",
)

engine = PromptImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    PromptImageGenerationClient(engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```
