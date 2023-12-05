## Overview

Image Generation Drivers are used by an Image Generation Engine to build and execute API calls to image generation models.

Use a driver to build an engine, then pass it to a tool for use by an Agent:

```python
from griptape.structures import Agent
from griptape.engines import ImageGenerationEngine
from griptape.drivers import OpenAiDalleImageGenerationDriver
from griptape.tools import ImageGenerator, FileManager

driver = OpenAiDalleImageGenerationDriver(
    model="dall-e-3",
)

engine = ImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    ImageGenerator(image_generation_engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

### Amazon Bedrock

The Amazon Bedrock image generation driver provides multi-model access to image generation models hosted by Amazon Bedrock. This driver manages the API calls to the Bedrock API, while the specific model drivers below format the API requests and parse the responses.

#### Amazon Bedrock Stable Diffusion Model Driver

The Amazon Bedrock Stable Diffusion model driver provides support for Stable Diffusion models hosted by Amazon Bedrock. This model driver supports configurations specific to Stable Diffusion, like style presets, clip guidance presets, sampler, and more.

```python
from griptape.structures import Agent
from griptape.tools import ImageGenerator, FileManager
from griptape.engines import ImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver
from griptape.drivers import AmazonBedrockStableDiffusionImageGenerationModelDriver

model_driver = AmazonBedrockStableDiffusionImageGenerationModelDriver(
    style_preset="cinematic",
    steps=50,
)

driver = AmazonBedrockImageGenerationDriver(
    model_driver=model_driver,
)

engine = ImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    ImageGenerator(image_generation_engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

#### Amazon Bedrock Titan Image Generator Model Driver

The Amazon Bedrock Titan Image Generator model driver provides support for Titan Image Generator models hosted by Amazon Bedrock. This model driver supports configurations specific to Titan Image Generator, like quality, seed, and cfg_scale.

```python
from griptape.structures import Agent
from griptape.tools import ImageGenerator, FileManager
from griptape.engines import ImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver
from griptape.drivers import AmazonBedrockTitanImageGeneratorImageGenerationModelDriver

model_driver = AmazonBedrockTitanImageGeneratorImageGenerationModelDriver(
    quality="hd",
)

driver = AmazonBedrockImageGenerationDriver(
    model_driver=model_driver,
)

engine = ImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    ImageGenerator(image_generation_engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

### Azure OpenAI DALL-E

The Azure OpenAI DALL-E image generation driver provides access to OpenAI DALL-E models hosted by Azure. In addition to the configurations provided by the underlying OpenAI DALL-E driver, the Azure OpenAI Dall-E Driver allows configuration of Azure-specific deployment values.

```python
from griptape.structures import Agent
from griptape.tools import ImageGenerator, FileManager
from griptape.engines import ImageGenerationEngine
from griptape.drivers import AzureOpenAiDalleImageGenerationDriver

driver = AzureOpenAiDalleImageGenerationDriver(
    model="dall-e-3",
    azure_deployment="my-azure-deployment",
    azure_endpoint="https://example-endpoint.openai.azure.com",
)

engine = ImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    ImageGenerator(image_generation_engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

### Leonardo.Ai

The Leonardo image generation driver enables image generation using models hosted by [Leonardo.ai](https://leonardo.ai/).

The Leonardo image generation driver supports configurations like model selection, image size, specifying a generation seed, and generation steps. For details on supported configuration parameters, see [Leonardo.Ai's image generation documentation](https://docs.leonardo.ai/reference/creategeneration). 

```python
import os 
from griptape.structures import Agent
from griptape.tools import ImageGenerator, FileManager
from griptape.engines import ImageGenerationEngine
from griptape.drivers import LeonardoImageGenerationDriver

driver = LeonardoImageGenerationDriver(
    model="6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",
    api_key=os.getenv("LEONARDO_API_KEY"),
    image_width=512,
    image_height=1024,
    seed=2213993,
)

engine = ImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    ImageGenerator(image_generation_engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```

### OpenAI DALL-E

The OpenAI DALL-E image generation driver enables image generation using OpenAI DALL-E models. Like other OpenAI drivers, the image generation driver will implicitly load an API key in the `OPENAI_API_KEY` environment variable if one is not explicitly provided.

The OpenAI Dall-E driver supports image generation configurations like style presets, image quality preference, and image size. For details on supported configuration values, see the [OpenAI documentation](https://platform.openai.com/docs/guides/images/introduction).

```python
from griptape.structures import Agent
from griptape.tools import ImageGenerator, FileManager
from griptape.engines import ImageGenerationEngine
from griptape.drivers import OpenAiDalleImageGenerationDriver

driver = OpenAiDalleImageGenerationDriver(
    model="dall-e-3"
    style="natural",
    quality="hd",
    image_size="1024x1792",
)

engine = ImageGenerationEngine(image_generation_driver=driver)

agent = Agent(tools=[
    ImageGenerator(image_generation_engine=engine),
    FileManager(),
])

agent.run("Generate a watercolor painting of a dog riding a skateboard. Save the image as rad-dog.png.")
```
