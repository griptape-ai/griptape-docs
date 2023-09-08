# FileManager

This tool enables LLMs to save and load files.

```python
from griptape.structures import Agent
from griptape.tools import FileManager

# Set up an agent using the FileManager tool
file_manager_tool = FileManager(dir='/path/to/files')
agent = Agent(
    tools=[file_manager_tool]
)

# Load files from disk
load_result = agent.run({
    "description": "Load specific files from disk",
    "tool": "FileManager",
    "activity": "load_files_from_disk",
    "values": {
        "paths": ["example_file.txt"]
    }
})

if isinstance(load_result, ErrorArtifact):
    print(f"Error occurred: {load_result}")
else:
    for artifact in load_result:
        print(f"Loaded {artifact.name} with content: {artifact.data.decode()}")
```
