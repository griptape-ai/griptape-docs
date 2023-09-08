# Calculator

This tool enables LLMs to make simple calculations.

```python
from griptape.structures import Agent
from griptape.tools import Calculator

# Initialize the Calculator tool
calculator = Calculator()

# Create an agent with the Calculator tool
agent = Agent(
    tools=[calculator]
)

# Run the agent with a task to perform the arithmetic calculation of \(10^5\)
result = agent.run({
    "expression": "10**5",
    "description": "Can be used for making simple numeric or algebraic calculations in Python"
})

print(result)
```
