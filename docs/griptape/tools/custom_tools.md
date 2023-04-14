# Custom Tools

Building your own tools is easy with Griptape! All you need is a Python class, YAML manifest, and a `requirements.txt` file. Let's walk through all the required steps and build a simple random number generator tool.

Let's start with creating a manifest file:

```yaml
version: "v1"
name: Random Number Generator
description: Tool for generating random numbers.
contact_email: hello@griptape.ai
legal_info_url: https://www.griptape.ai/legal
```

Manifest files are for humans and downstream systems, like ChatGPT Plugins, to generate manifests of their own.

Next, create a `tool.py` file with the following class:

```python
from attr import define, field
from schema import Schema, Literal
from griptape.core import BaseTool, action
import random


@define
class RandomNumberGenerator(BaseTool):
    configs = {
        "test": {
            "name": "generate",
            "description": "Can be used to generate random numbers",
            "value_schema": Schema({
                Literal(
                    "value",
                    description="The number of decimals to be considered while rounding"
                ): str
            })
        }
    }

    test_field: str = field(default="test", kw_only=True, metadata={"env": "TEST_FIELD"})

    @action(config=configs["test"])
    def generate(self, value: bytes) -> str:
        return round(random.random(), int(value.decode()))

```

Also, add an empty `__init__.py` file next to `tool.py`, so that the tool directory is correctly interpreted by Python.

Finally, add a `requirements.txt` file:

```
griptape-core
```

Now, let's test the tool:

```python
LocalExecutor().execute(RandomNumberGenerator().generate, "2".encode())
```

That's it! You can start using this tool with any adapter or directly via Skatepark.

Check out other [Griptape tools](https://github.com/griptape-ai/griptape-tools/tree/main/griptape/tools) to learn more about tool implementation details.