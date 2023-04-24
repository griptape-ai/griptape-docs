# Workflows

Workflows are non-sequential DAGs that can be used for complex concurrent scenarios with steps having multiple inputs.


Steps in the workflow have access to a different set of `context` variables:

- `args`: arguments passed to the `Construct.run()` method.
- `inputs`: inputs into the current step referencable by parent step IDs.
- `structure`: the structure that the step belongs to.
- `parents`: parent steps referencable by IDs.
- `children`: child steps referencable by IDs.

Let's build a simple workflow. Let's say, we want to write a story in a fantasy world with some unique characters. We could setup a workflow that generates a world based on some keywords. Then we pass the world description to any number of child steps that create characters. Finally, the last step pulls in information from all parent steps and writes up a short story.

```python
def character_step(step_id, character_name) -> PromptTask:
    return PromptTask(
        "Based on the following world description create a character named {{ name }}:\n{{ inputs['world'] }}",
        context={
            "name": character_name
        },
        id=step_id
    )

world_step = PromptTask(
    "Create a fictional world based on the following key words {{ keywords|join(', ') }}",
    context={
        "keywords": ["fantasy", "ocean", "tidal lock"]
    },
    id="world"
)

character_step_1 = character_step("scotty", "Scotty")
character_step_2 = character_step("annie", "Annie")

story_step = PromptTask(
    "Based on the following description of the world and characters, write a short story:\n{{ inputs['world'] }}\n{{ inputs['scotty'] }}\n{{ inputs['annie'] }}",
    id="story"
)

workflow = Workflow()

workflow.add_task(world_step)

world_step.add_child(character_step_1)
world_step.add_child(character_step_2)
world_step.add_child(story_step)

character_step_1.add_child(story_step)
character_step_2.add_child(story_step)

workflow.run()

[print(step.output.value) for step in workflow.output_steps()]
```

And here is the beginning of our generated story:

> Scotty and Annie had been friends since childhood, and their bond had only grown stronger over the years. Scotty had always been fascinated by the ocean and its secrets, and Annie had always been drawn to its magical creatures. [...]