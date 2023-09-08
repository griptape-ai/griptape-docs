# Computer

This tool enables LLMs to execute Python code and run shell commands inside a Docker container. You have to have the Docker daemon running in order for this tool to work.

You can specify a local working directory and environment variables during tool initialization:

```python
from griptape.structures import Agent
from griptape.tools import Computer

# Initialize the Computer tool
computer = Computer()

# Create an agent with the Computer tool
agent = Agent(
    tools=[computer]
)

# Execute a shell command to list files in the container
result = agent.run({
    "command": "ls -la",
    "description": "List all files and directories in the root of the container"
})

print(result)
```
