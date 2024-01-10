## Overview

Image generation engines facilitate the use of [image generation drivers](../structures/image-generation-drivers.md) by image generation tasks and tools. Each image generation engine defines a `run` method that accepts the inputs necessary for each image generation mode and provides the request to the configured image generation driver.

#### Rulesets

[Rulesets](../structures/rulesets.md) provided to image generation engines are combined with prompts, providing further instruction to image generation models. In addition to typical Rulesets, image generation engines support Negative Rulesets as arguments to their `run()` methods. Negative Rulesets are used by [image generation drivers](../structures/image-generation-drivers.md) with support for prompt weighting and used to influence the image generation model to avoid undesirable features and characteristics described by negative prompts.

### Prompt Image Generation Engine 

This image generation engine facilitates generating images from text prompts.

```python
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tools import PromptImageGenerationClient


# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = PromptImageGenerationEngine(
    image_generation_driver=driver,
)

# Create a tool configured to use the engine.
tool = PromptImageGenerationClient(
    engine=engine,
)
```

### Variation Image Generation Engine 

This image generation engine facilitates generating variations of an input image according to a text prompt.

```python
from griptape.engines import VariationImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tools import VariationImageGenerationClient


# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = VariationImageGenerationEngine(
    image_generation_driver=driver,
)

# Create a tool configured to use the engine.
tool = VariationImageGenerationClient(
    engine=engine,
)
```

### Inpainting Image Generation Engine

This image generation engine facilitates image inpainting, or modifying an input image according to a text prompt within the bounds of a mask defined by mask image.

```python
from griptape.engines import InpaintingImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tools import InpaintingImageGenerationClient


# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = InpaintingImageGenerationEngine(
    image_generation_driver=driver,
)

# Create a tool configured to use the engine.
tool = InpaintingImageGenerationClient(
    engine=engine,
)
```

### Outpainting Image Generation Engine

This image generation engine facilitates image outpainting, or modifying an input image according to a text prompt outside the bounds of a mask defined by a mask image.

```python
from griptape.engines import OutpaintingImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tools import OutpaintingImageGenerationClient


# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = OutpaintingImageGenerationEngine(
    image_generation_driver=driver,
)

# Create a tool configured to use the engine.
tool = OutpaintingImageGenerationClient(
    engine=engine,
)
```
