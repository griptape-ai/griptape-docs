# Memory

Griptape supports different types of memory for pipelines. Due to the non-linear nature of workflows you can't use memory with them yet, but we are currently investigating other possibilities.

By default, pipelines don't initialize memory, so you have to explicitly pass it to them:

```python
Pipeline(
    memory=ConversationMemory()
)
```

There are two other types of memory: `BufferMemory` and `SummaryMemory`. `BufferMemory` will keep a sliding window of tasks that are used to construct a prompt:

```python
Pipeline(
    memory=BufferMemory(buffer_size=3)
)
```

This works great for shorter pipelines but fails if the whole workflow context needs to be present. You can use `SummaryMemory` to address that:

```python
Pipeline(
    memory=SummaryMemory(
        summarizer=PromptDriverSummarizer(
            driver=OpenAiPromptDriver()
        ),
        offset=2
    )
)
```

This will progressively summarize the whole pipeline except for the last two tasks.

Finally, you can persist memory by using memory drivers. Griptape comes with one memory driver for automatically storing memory in a file on the disk. Here is how you can initialize memory with a driver:

```python
Memory(
    driver=DiskMemoryDriver(file_path="memory.json")
)
```

To load memory:

```python
DiskMemoryDriver(file_path="memory.json").load()
```

You can easily build drivers for your own data stores by extending `MemoryDriver`. You only need to implement `store` and `load` methods.