# Prompt Drivers

Prompt drivers are used by **griptape** structures to make calls to the underlying foundation models. **OpenAiPromptDriver** is the default prompt driver used in all structures.

You can instantiate drivers and pass them to structures:

```python
Pipeline(
    prompt_driver=OpenAiPromptDriver(
        model="gpt-4"
    )
)
```

Or use them independently:

```python
OpenAiPromptDriver(
    model="gpt-4"
).run("Q: give me some ideas for writing a fantasy book\nA:")
```
