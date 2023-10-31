# Overview 
Extraction Engines in Griptape facilitate the extraction of data from text formats such as CSV and JSON.
These engines play a crucial role in the functionality of [Extraction Tasks](../../griptape-framework/structures/tasks.md).
As of now, Griptape supports two types of Extraction Engines: the CSV Extraction Engine and the JSON Extraction Engine.

## CSV Extraction Engine

The CSV Extraction Engine is designed specifically for extracting data from CSV-formatted content.

!!! info
  The CSV Extraction Engine requires the `column_names` parameter for specifying the columns to be extracted.

```python
from griptape.engines import CsvExtractionEngine
from griptape.artifacts import ListArtifact, ErrorArtifact

# Initialize the CsvExtractionEngine instance
csv_engine = CsvExtractionEngine()

# Given a sample text which contains CSV content
sample_text = """
name, age, location
Alice, 28, New York
Bob, 35, California
Charlie, 40, Texas
"""

# Extract CSV rows using the engine
result = csv_engine.extract(sample_text, column_names=["name", "age", "location"])

# Check and display the result
if isinstance(result, ListArtifact):
    for row in result.value:
        print(row.value)  # This will print each row in the CSV content
elif isinstance(result, ErrorArtifact):
    print(f"Error: {result.value}")  # Print error if there's any issue in extraction
```
```
{'name': 'name, age, location'}
{'name': 'Alice, 28, New York'}
{'name': 'Bob, 35, California'}
{'name': 'Charlie, 40, Texas'}
```

## JSON Extraction Engine

The JSON Extraction Engine is tailored for extracting data from JSON-formatted content. 

!!! info
  The JSON Extraction Engine requires the `template_schema` parameter for specifying the structure to be extracted.

```python
from griptape.engines import JsonExtractionEngine
from griptape.artifacts import ListArtifact, ErrorArtifact
from schema import Schema

json_engine = JsonExtractionEngine()

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
user_schema = Schema(
    {"users": [{"name": str, "age": int, "location": str}]}
).json_schema("UserSchema")

# Extract data using the engine
result = json_engine.extract(sample_json_text, template_schema=user_schema)

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
