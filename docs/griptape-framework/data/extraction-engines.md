# Overview 
Extraction Engines are used to extract data from text formats like CSV, JSON, etc. They are mainly used for [Extraction Tasks](../../griptape-framework/structures/tasks.md).
There are two types of extraction engines in Griptape: CSV Extraction Engine and JSON Extraction Engine.

## CSV Extraction Engine

Used to extract data from a CSV file. You can set a custom [Prompt driver](../../griptape-framework/structures/prompt-drivers.md) or [Chunker](../../griptape-framework/data/chunkers.md). 
You can use it along with [Extraction Tasks](../../griptape-framework/structures/tasks.md)

```python
from griptape.engines import CsvExtractionEngine
from griptape.artifacts import ListArtifact, ErrorArtifact
from griptape.drivers import OpenAiChatPromptDriver

# Initialize the CsvExtractionEngine instance
csv_engine = CsvExtractionEngine(prompt_driver=OpenAiChatPromptDriver(model="gpt-4", temperature=0.3))

# Given a sample text which contains CSV content
sample_text = """
name, age, location
Alice, 28, New York
Bob, 35, California
Charlie, 40, Texas
"""

# Extract CSV rows using the engine
result = csv_engine.extract(sample_text, column_names=['name', 'age', 'location'])

# Check and display the result
if isinstance(result, ListArtifact):
    for row in result.value:
        print(row)  # This will print each row in the CSV content
elif isinstance(result, ErrorArtifact):
    print(f"Error: {result.value}")  # Print error if there's any issue in extraction
```
```
{"id": "c0aa68f91f5e4368b784b7e20c5187bc", "name": "c0aa68f91f5e4368b784b7e20c5187bc", "type": "CsvRowArtifact", "value": {"name": "Alice", "age": "\"28\"", "location": "\"New York\""}}
{"id": "1e02e3609eb3443cbe5072830515999f", "name": "1e02e3609eb3443cbe5072830515999f", "type": "CsvRowArtifact", "value": {"name": "Bob", "age": "\"35\"", "location": "\"California\""}}
{"id": "a685dc0d9cd24feb9c08f9010dce0387", "name": "a685dc0d9cd24feb9c08f9010dce0387", "type": "CsvRowArtifact", "value": {"name": "Charlie", "age": "\"40\"", "location": "\"Texas\""}}
```

## JSON Extraction Engine

Used to extract data from a JSON file. You can set a custom [Prompt driver](../../griptape-framework/structures/prompt-drivers.md) or [Chunker](../../griptape-framework/data/chunkers.md). 
You can use it along with [Extraction Tasks](../../griptape-framework/structures/tasks.md)

```python
from griptape.engines import JsonExtractionEngine
from griptape.artifacts import ListArtifact, ErrorArtifact
from griptape.drivers import OpenAiChatPromptDriver

json_engine = JsonExtractionEngine(prompt_driver=OpenAiChatPromptDriver(model="gpt-4", temperature=0.3))

# Given a sample JSON text
sample_json_text = """
{
  "users": [
    {
      "name": "Alice",
      "age": 28,
      "location": "New York"
    },
    {
      "name": "Bob",
      "age": 35,
      "location": "California"
    }
  ]
}
"""

# Define a schema for extraction
template_schema = {
    "users": [{
        "name": None,
        "age": None,
        "location": None
    }]
}

# Extract data using the engine
result = json_engine.extract(sample_json_text, template_schema=template_schema)

# Check and display the result
if isinstance(result, ListArtifact):
    for artifact in result.value:
        print(artifact.value)  # This will print each extracted artifact
elif isinstance(result, ErrorArtifact):
    print(f"Error: {result.value}")  # Print error if there's any issue in extraction

```
```
{'name': 'Alice', 'age': 28, 'location': 'New York'}
{'name': 'Bob', 'age': 35, 'location': 'California'}
```