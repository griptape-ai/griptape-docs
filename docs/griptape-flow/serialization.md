# Serialization

Workflows and pipelines can be serialized into Python dictionaries and JSON strings:

```python
pipeline = Pipeline()

pipeline.add_step(PromptStep())

pipeline.to_dict()
# or
pipeline.to_json()
```

You can also load workflows and pipelines from Python dictionaries and JSON strings:

```python
Pipeline.from_dict(pipeline_dict)
# or
Pipeline.from_json(pipeline_json)
```

griptape-flow uses [Marshmallow](https://github.com/marshmallow-code/marshmallow/) schemas for serialization and deserialization.

To load a workflow from a file, first add workflow JSON to a file (e.g., `workflow.json`):

```json
{
  "prompt_driver": {
    "temperature": 0.5,
    "type": "OpenAiPromptDriver"
  },
  "steps": [
    {
      "id": "world",
      "type": "PromptStep",
      "parent_ids": [],
      "child_ids": [
        "scotty",
        "annie"
      ],
      "prompt_template": "Create a fictional world based on the following key words {{ keywords|join(', ') }}",
      "context": {
        "keywords": [
          "fantasy",
          "ocean",
          "tidal lock"
        ]
      }
    },
    ...
  ]
}
```

Then load it with:

```python
with open("workflow.json", "r") as file:
    workflow = Workflow.from_json(file.read())

    workflow.run()
```

It's important to note that `ToolLoader` and `PipelineMemory` are not serializable/deserializable, so you have to connect them manually.