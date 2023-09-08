# DateTime

This tool enables LLMs to get current date and time.

```python
from griptape.structures import Agent
from griptape.tools import DateTime

# Initialize the DateTime tool
datetime_tool = DateTime()

# Create an agent with the DateTime tool
agent = Agent(
    tools=[datetime_tool]
)

# Fetch the current date and time
result = agent.run({
    "description": "Fetch the current date and time using the DateTime tool"
})

print(f"The current date and time is: {result}")
```
