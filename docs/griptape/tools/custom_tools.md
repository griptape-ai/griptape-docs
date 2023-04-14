# Custom Tools

Building your own tools is easy with Griptape! All you need is a Python class, YAML manifest, and a `requirements.txt` file. Let's walk through all the required steps and build a simple random number generator tool.

Let's start with creating a manifest file:

```yaml
version: "v1"
name: Mock Tool
description: Tool for griptape tests
contact_email: hello@griptape.ai
legal_info_url: https://www.griptape.ai/legal
```

Next, create a Python class in a separate directory that generates a random float and optionally truncates it:

```python
from attr import define, field
from schema import Schema, Literal
from griptape.core import BaseTool, action


@define
class MockTool(BaseTool):
    configs = {
        "test": {
            "name": "test",
            "description": "test description: {{ foo }}",
            "value_schema": Schema({
                Literal(
                    "value",
                    description="Test input"
                ): str
            }),
            "foo": "bar"
        }
    }

    test_field: str = field(default="test", kw_only=True, metadata={"env": "TEST_FIELD"})

    @action(config=configs["test"])
    def test(self, value: bytes) -> str:
        return f"ack {value.decode()}"

    @property
    def schema_template_args(self) -> dict:
        return {
            "foo": "bar"
        }
```

Create an empty `__init__.py` file, so that the tool directory is correctly interpreted by Python.

Finally, add a `requirements.txt` file:

```
griptape-core
```

Now, let's use the tool:

```python
# WIP
```

Check out other [Griptape tools](https://github.com/griptape-ai/griptape-tools/tree/main/griptape/tools) to learn more about tool implementation details.