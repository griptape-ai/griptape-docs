## Overview

Image generation Engines facilitate the use of [image generation drivers](../structures/image-generation-drivers.md) by image generation Tasks and Tools. Each image generation Engine defines a `run` method that accepts the inputs necessary for its image generation mode and provides the request to the configured Driver.

### Image Generation Engine Rulesets

[Rulesets](../structures/rulesets.md) provided to image generation Engines are combined with prompts, providing further instruction to image generation models. In addition to typical Rulesets, image generation Engines support Negative Rulesets as arguments to their `run()` methods. Negative Rulesets are used by [image generation drivers](../structures/image-generation-drivers.md) with support for prompt weighting and used to influence the image generation model to avoid undesirable features and characteristics described by negative prompts.

### Prompt Image Generation Engine 

This Engine facilitates generating images from text prompts.

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

engine.run(
    prompts=["A watercolor painting of a dog riding a skateboard"],
)
```

### Variation Image Generation Engine 

This Engine facilitates generating variations of an input image according to a text prompt.

```python
from griptape.engines import VariationImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.loaders import ImageLoader

# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = VariationImageGenerationEngine(
    image_generation_driver=driver,
)

engine.run(
    prompts=["A photo of a mountain landscape in winter"],
    image=ImageLoader().load("mountain.png"),
)
```

### Inpainting Image Generation Engine

This Engine facilitates image inpainting, or modifying an input image according to a text prompt within the bounds of a mask defined by mask image.

```python
from griptape.engines import InpaintingImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.loaders import ImageLoader


# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = InpaintingImageGenerationEngine(
    image_generation_driver=driver,
)

engine.run(
    prompts=["A photo of a mountain landscape in winter"],
    image=ImageLoader().load("mountain.png"),
    mask=ImageLoader().load("mountain-mask.png"),
)
```

### Outpainting Image Generation Engine

This Engine facilitates image outpainting, or modifying an input image according to a text prompt outside the bounds of a mask defined by a mask image.

```python
from griptape.engines import OutpaintingImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.loaders import ImageLoader

# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = OutpaintingImageGenerationEngine(
    image_generation_driver=driver,
)

engine.run(
    prompts=["A photo of a mountain landscape in winter"],
    image=ImageLoader().load("mountain.png"),
    mask=ImageLoader().load("mountain-mask.png"),
)
```
