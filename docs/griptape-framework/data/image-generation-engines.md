## Overview

Image generation engines facilitate the use of [image generation drivers](../structures/image-generation-drivers.md) by image generation tasks and tools. Each image generation engine defines a `run` method that accepts the inputs necessary for each image generation mode, combines these inputs with any available rulesets, and provides the request to the configured image generation driver.

#### Rulesets

[Rulesets](../structures/rulesets.md) provided to image generation engines are combined with prompts, providing further instruction to image generation models. In addition to typical Rulesets, image generation engines support Negative Rulesets. Negative Rulesets are used by [image generation drivers](../structures/image-generation-drivers.md) with support for prompt wieghting and used to influence the image generation model to avoid undesireable features described by negative prompts.

### Prompt Image Generation Engine 

This image generation engine facilitates generating images from text prompts.

```python
from griptape.structures import Agent
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tools import PromptImageGenerationClient


# Define positive and negative rulesets.
positive_ruleset = Ruleset(rules=[Rule("realistic"), Rule("high quality")])
negative_ruleset = Ruleset(rules=[Rule("distorted")])

# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = PromptImageGenerationEngine(
    rulesets=[positive_ruleset],
    negative_rulesets=[negative_ruleset],
    image_generation_driver=driver,
)

# Create a tool configured to use the engine.
tool = PromptImageGenerationClient(
    image_generation_engine=engine,
)
```

### Variation Image Generation Engine 

This image generation engine facilitates generating variations of an input image according to a text prompt.

```python
from griptape.structures import Agent
from griptape.engines import VariationImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tools import VariationImageGenerationClient


# Define positive and negative rulesets.
positive_ruleset = Ruleset(rules=[Rule("realistic"), Rule("high quality")])
negative_ruleset = Ruleset(rules=[Rule("distorted")])

# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = VariationImageGenerationEngine(
    rulesets=[positive_ruleset],
    negative_rulesets=[negative_ruleset],
    image_generation_driver=driver,
)

# Create a tool configured to use the engine.
tool = VariationImageGenerationClient(
    image_generation_engine=engine,
)
```

### Inpainting Image Generation Engine

This image generation engine facilitates image inpainting, or modifying an input image according to a text prompt within the bounds of a mask defined by mask image.

```python
from griptape.structures import Agent
from griptape.engines import InpaintingImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tools import InpaintingImageGenerationClient


# Define positive and negative rulesets.
positive_ruleset = Ruleset(rules=[Rule("realistic"), Rule("high quality")])
negative_ruleset = Ruleset(rules=[Rule("distorted")])

# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = InpaintingImageGenerationEngine(
    rulesets=[positive_ruleset],
    negative_rulesets=[negative_ruleset],
    image_generation_driver=driver,
)

# Create a tool configured to use the engine.
tool = InpaintingImageGenerationClient(
    image_generation_engine=engine,
)
```

### Outpainting Image Generation Engine

This image generation engine facilitates image outpainting, or modifying an input image according to a text prompt outside the bounds of a mask defined by a mask image.

```python
from griptape.structures import Agent
from griptape.engines import OutpaintingImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tools import OutpaintingImageGenerationClient


# Define positive and negative rulesets.
positive_ruleset = Ruleset(rules=[Rule("realistic"), Rule("high quality")])
negative_ruleset = Ruleset(rules=[Rule("distorted")])

# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = OutpaintingImageGenerationEngine(
    rulesets=[positive_ruleset],
    negative_rulesets=[negative_ruleset],
    image_generation_driver=driver,
)

# Create a tool configured to use the engine.
tool = OutpaintingImageGenerationClient(
    image_generation_engine=engine,
)
```
