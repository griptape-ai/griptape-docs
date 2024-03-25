# ImageQueryClient

This tool allows Agents to execute natural language queries on the contents of images using multimodal models.

```python
from griptape.structures import Agent
from griptape.tools import ImageQueryClient
from griptape.drivers import OpenAiVisionImageQueryDriver
from griptape.engines import ImageQueryEngine 

# Create an Image Query Driver.
driver = OpenAiVisionImageQueryDriver(
    model="gpt-4-vision-preview"
)
    
# Create an Image Query Engine configured to use the driver.
engine = ImageQueryEngine(
    image_query_driver=driver,
)

# Create an Image Query Client configured to use the engine.
tool = ImageQueryClient(
    image_query_engine=engine,
    off_prompt=False,
)

# Create an agent and provide the tool to it.
Agent(tools=[tool]).run("Describe the weather in the image tests/assets/mountain.png in one word.")
```
