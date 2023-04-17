# Custom Tools

Building your own tools is easy with Griptape!

To start, create a directory for your tool inside your project. All tool directories should have the following components:

- `manifest.yml` with a YAML manifest.
- `tool.py` file with a tool Python class.
- `requirements.txt` file with tool Python dependencies.
- Optional `Dockerfile` if you are using `DockerExecutor` to run your tool, and you want to install custom OS-level packages.

Let's build a simple random number generator tool! First, create a new directory for your tool `rng_tool`. This is where all tool files will go.

## Tool Manifest

Tool YAML manifests are for humans and downstream systems, like ChatGPT Plugins, to generate manifests of their own. Create a `manifest.yml` file in the `rng_tool` directory:

```yaml
version: "v1"
name: Random Number Generator
description: Tool for generating random numbers.
contact_email: hello@griptape.ai
legal_info_url: https://www.griptape.ai/legal
```

## Tool Dependencies

To add Python dependencies for your tool, add a `requirements.txt` file:

```
griptape-core>=0.8.0
```

## Tool Implementation

Next, create a `tool.py` file with the following code:

```python
import random
from griptape.core import BaseTool, action
from schema import Schema


class RandomNumberGenerator(BaseTool):
    @action(config={
            "name": "generate",
            "description": "Can be used to generate random numbers",
            "schema": Schema(
                int,
                description="Number of decimals to round the random number to"
            )
        })
    def generate(self, value: bytes) -> str:
        return str(round(random.random(), int(value.decode())))
```

## Testing Custom Tools

Finally, let's test our tool:

```python
from skatepark.steps import ToolkitStep
from skatepark.structures import Pipeline
from skatepark.utils import ToolLoader
from rng_tool.tool import RandomNumberGenerator


rng_tool = RandomNumberGenerator()

pipeline = Pipeline(
    tool_loader=ToolLoader(
        tools=[rng_tool]
    )
)

pipeline.add_steps(
    ToolkitStep(
        tool_names=[rng_tool.name]
    )
)

print(
    pipeline.run(
        "generate a random number rounded to 5 decimal places"
    ).output.value
)

```

That's it! You can start using this tool with any adapter or directly via Skatepark.

Check out other [Griptape tools](https://github.com/griptape-ai/griptape-tools/tree/main/griptape/tools) to learn more about tool implementation details.