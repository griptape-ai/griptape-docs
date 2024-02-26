## Overview
Extraction Engines in Griptape facilitate the extraction of data from text formats such as CSV and JSON.
These engines play a crucial role in the functionality of [Extraction Tasks](../../griptape-framework/structures/tasks.md).
As of now, Griptape supports two types of Extraction Engines: the CSV Extraction Engine and the JSON Extraction Engine.

## CSV Extraction Engine

The CSV Extraction Engine is designed specifically for extracting data from CSV-formatted content.

!!! info
    The CSV Extraction Engine requires the `column_names` parameter for specifying the columns to be extracted.

```python
import os 

from griptape.drivers import AzureOpenAiChatPromptDriver
from griptape.engines import CsvExtractionEngine

# Initialize a prompt driver
prompt_driver = AzureOpenAiChatPromptDriver(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    model="gpt-3.5-turbo-16k",
    azure_deployment=os.environ["AZURE_OPENAI_35_TURBO_16k_DEPLOYMENT_ID"],
    azure_endpoint=os.environ["AZURE_OPENAI_API_BASE"],
)

# Initialize the CsvExtractionEngine instance
csv_engine = CsvExtractionEngine(
    prompt_driver=prompt_driver,
)

# Define some unstructured data
sample_text = """
Alice, 28, lives in New York.
Bob, 35 lives in California.
Charlie is 40 and lives in Texas.
"""

# Extract CSV rows using the engine
result = csv_engine.extract(sample_text, column_names=["name", "age", "location"])

for row in result.value:
    print(row.to_text())
```
```
name,age,location
Alice,28,New York
Bob,35,California
Charlie,40,Texas
```

## JSON Extraction Engine

The JSON Extraction Engine is tailored for extracting data from JSON-formatted content. 

!!! info
    The JSON Extraction Engine requires the `template_schema` parameter for specifying the structure to be extracted.

```python
import os 
from schema import Schema 

from griptape.drivers import AzureOpenAiChatPromptDriver
from griptape.engines import JsonExtractionEngine

# Initialize a prompt driver
prompt_driver = AzureOpenAiChatPromptDriver(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    model="gpt-3.5-turbo-16k",
    azure_deployment=os.environ["AZURE_OPENAI_35_TURBO_16k_DEPLOYMENT_ID"],
    azure_endpoint=os.environ["AZURE_OPENAI_API_BASE"],
)

json_engine = JsonExtractionEngine(prompt_driver=prompt_driver)

# Define some unstructured data
sample_json_text = """
Alice (Age 28) lives in New York.
Bob (Age 35) lives in California.
"""

# Define a schema for extraction
user_schema = Schema(
    {"users": [{"name": str, "age": int, "location": str}]}
).json_schema("UserSchema")

# Extract data using the engine
result = json_engine.extract(sample_json_text, template_schema=user_schema)

for artifact in result.value:
    print(artifact.value)
```
```
{'name': 'Alice', 'age': 28, 'location': 'New York'}
{'name': 'Bob', 'age': 35, 'location': 'California'}
```
