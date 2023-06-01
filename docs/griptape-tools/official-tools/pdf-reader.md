# PdfReader

This tool enables LLMs to read the text content of a PDF.

```python
from griptape.tools import PdfReader
from griptape.memory.structure import ConversationMemory
from griptape.tasks import ToolkitTask
from griptape.structures import Pipeline

pdf_reader = PdfReader("https://github.com/griptape-ai/griptape-tools/blob/fccf9d1a34d8b6adc04773d048d8a0463b725418/tests/unit/bitcoin.pdf")

pipeline = Pipeline(
    memory=ConversationMemory()
)

pipeline.add_tasks(
    ToolkitTask(
        tools=[pdf_reader]
    )
)

result = pipeline.run("What is the maximum number of bitcoins created?")
print(result.output.value)

```

You should see a final result similar to the following: 

```
Input: Read this .../tests/unit/bitcoin.pdf. Summarise the limits on the number ofbitcoins created and the timescales

[chain of thought output... will vary depending on the model driver you're using]

Output: The Bitcoin system has a limit on the number of bitcoins that can be created, which is set at 21
million. This limit is enforced by the protocol, and it ensures that there will never be more than 21 million
bitcoins in existence. The rate at which new bitcoins are created is also controlled by the protocol, and it
gradually decreases over time. This process is known as "halving," and it occurs approximately every four
years. Currently, the block reward for successfully mining a block is 6.25 bitcoins. <snip>
```
