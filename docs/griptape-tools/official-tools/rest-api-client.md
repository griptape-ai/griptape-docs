# RestApiClient

This tool enables LLMs to call REST APIs.

The **RestApiClient** tool uses the following parameters: 

| Parameter      | Description                          | Required |
| ----------- | ------------------------------------ |----------|
| `base_url`  | The base url that will be used for the request. | YES |
| `path`       | The resource path that will be appended to `base_url`. | YES |
| `description`    | A description of what the REST API does.  | YES |
| `request_body_schema` | A JSON schema string describing the request body. Recommended for PUT, POST, and PATCH requests. | NO |
| `request_query_params_schema` | A JSON schema string describing the available query parameters. | NO |
| `request_path_params_schema` | A JSON schema string describing the available path parameters. The schema must describe an array of string values. | NO |
| `response_body_schema` | A JSON schema string describing the response body. | NO |

### Example
The following example is built using [https://jsonplaceholder.typicode.com/guide/](https://jsonplaceholder.typicode.com/guide/).
  
```python
from json import dumps
from griptape.drivers import OpenAiPromptDriver
from griptape.memory.structure import ConversationMemory
from griptape.structures import Pipeline
from griptape.tasks import ToolkitTask
from griptape.tools import RestApiClient
from griptape.memory.tool import TextToolMemory

text_memory = TextToolMemory()
posts_client = RestApiClient(
    base_url="https://jsonplaceholder.typicode.com",
    path="posts",
    description="Allows for creating, updating, deleting, patching, and getting posts.",
    output_memory={
        "get": [text_memory]
    },
    input_memory={
        "get": [text_memory]
    },
    request_body_schema=dumps(
        {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "http://example.com/example.json",
            "type": "object",
            "default": {},
            "title": "Root Schema",
            "required": ["title", "body", "userId"],
            "properties": {
                "title": {
                    "type": "string",
                    "default": "",
                    "title": "The title Schema",
                },
                "body": {
                    "type": "string",
                    "default": "",
                    "title": "The body Schema",
                },
                "userId": {
                    "type": "integer",
                    "default": 0,
                    "title": "The userId Schema",
                },
            },
        }
    ),
    request_query_params_schema=dumps(
        {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "http://example.com/example.json",
            "type": "object",
            "default": {},
            "title": "Root Schema",
            "required": ["userId"],
            "properties": {
                "userId": {
                    "type": "string",
                    "default": "",
                    "title": "The userId Schema",
                },
            },
        }
    ),
    request_path_params_schema=dumps(
        {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "http://example.com/example.json",
            "type": "array",
            "default": [],
            "title": "Root Schema",
            "items": {
                "anyOf": [
                    {
                        "type": "string",
                        "title": "Post id",
                    },
                ]
            },
        }
    ),
    response_body_schema=dumps(
        {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "http://example.com/example.json",
            "type": "object",
            "default": {},
            "title": "Root Schema",
            "required": ["id", "title", "body", "userId"],
            "properties": {
                "id": {
                    "type": "integer",
                    "default": 0,
                    "title": "The id Schema",
                },
                "title": {
                    "type": "string",
                    "default": "",
                    "title": "The title Schema",
                },
                "body": {
                    "type": "string",
                    "default": "",
                    "title": "The body Schema",
                },
                "userId": {
                    "type": "integer",
                    "default": 0,
                    "title": "The userId Schema",
                },
            },
        }
    ),
)

pipeline = Pipeline(
    memory=ConversationMemory(),
    prompt_driver=OpenAiPromptDriver(
        temperature=0.1
    ),

)

pipeline.add_tasks(
    ToolkitTask(
        "Output the title of post 1.",
        tools=[posts_client],
    ),
    ToolkitTask(
        "Output the titles of all posts.",
        tools=[posts_client],
    ),
    ToolkitTask(
        "Create a post for user 1 with title 'My First Post' and body 'Hello world!'.",
        tools=[posts_client],
    ),
    ToolkitTask(
        "Update post 1 with a new body: 'Hello universe!'.",
        tools=[posts_client],
    ),
    ToolkitTask(
        "Patch post 1 with a new title: 'My First Post, A Journey'.",
        tools=[posts_client],
    ),
    ToolkitTask(
        "Delete post 1.",
        tools=[posts_client],
    ),
    ToolkitTask(
        "Output the body of all the comments for post 1.",
        tools=[posts_client],
    ),
)

pipeline.run()
```
