Tools give the LLM abilities to invoke outside APIs, reference data sets, and generally expand their capabilities.

Griptape tools are just Python classes with a decorator to help instruct the LLM on how to use the tool. Here is an example tool for generating a random number:

```python
import random
from griptape.artifacts import TextArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity
from schema import Schema, Literal, Optional


class RandomNumberGenerator(BaseTool):
    @activity(config={
            "description": "Can be used to generate random numbers",
            "schema": Schema({
                Optional(Literal(
                    "decimals",
                    description="Number of decimals to round the random number to"
                )): int
            })
        })
    def generate(self, params: dict) -> TextArtifact:
        return TextArtifact(
            str(round(random.random(), params["values"].get("decimals")))
        )
```

A tool can have many "activities" as denoted by the `@activity` decorator. Each activity has a description (used to provide context to the LLM), and the input schema that the LLM must follow in order to use the tool.

We provide a set of official Griptape Tools for accessing and processing data. You can also [build your own tools](./custom-tools/index.md).
