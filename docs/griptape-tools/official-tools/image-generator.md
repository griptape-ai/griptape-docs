# ImageGenerator

The ImageGenerator tool enables LLMs to generate images.

```python
from griptape.structures import Agent
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    AmazonBedrockStableDiffusionImageGenerationModelDriver
from griptape.engines import ImageGenerationEngine
from griptape.tools import ImageGenerator

# Initialize an Image Generation Driver
image_generation_driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=AmazonBedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Initialize the Image Generation Engine
image_generation_engine = ImageGenerationEngine(
    image_driver=image_generation_driver,
)

# Initialize the ImageGenerator
image_generator = ImageGenerator(
    image_generation_engine=image_generation_engine,
)

# Add the tool to the Agent
agent = Agent(
    tools=[image_generator]
)

# Provide the tool with an image generation prompt
agent.run("Generate an image of a beautiful mountain landscape on a summer day")
```
