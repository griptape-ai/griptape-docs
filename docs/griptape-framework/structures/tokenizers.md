## Overview 

Tokenizers are used throughout Griptape to calculate the number of [tokens](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/tokens) in a piece of text.
They are particulary useful for ensuring that the LLM token limits are not exceeded.

Tokenizers are a low level abstraction that you will rarely interact with directly.

## Tokenizers

### OpenAI

```python
from griptape.tokenizers import OpenAiTokenizer


tokenizer = OpenAiTokenizer(model=OpenAiTokenizer.DEFAULT_OPENAI_GPT_4_MODEL)

print(tokenizer.count_tokens("Hello world!"))  # 3
print(tokenizer.count_tokens_left("Hello world!"))  # 8181
```

### Cohere
```python
import os
from cohere import Client
from griptape.tokenizers import CohereTokenizer


tokenizer = CohereTokenizer(
    model=CohereTokenizer.DEFAULT_MODEL, client=Client(os.environ["COHERE_API_KEY"])
)

print(tokenizer.count_tokens("Hello world!"))  # 3
print(tokenizer.count_tokens_left("Hello world!"))  # 2045
```

### Anthropic

```python
from griptape.tokenizers import AnthropicTokenizer


tokenizer = AnthropicTokenizer(model=AnthropicTokenizer.DEFAULT_MODEL)

print(tokenizer.count_tokens("Hello world!"))  # 2
print(tokenizer.count_tokens_left("Hello world!"))  # 99997
```

### Hugging Face
```python
from transformers import AutoTokenizer
from griptape.tokenizers import HuggingFaceTokenizer


tokenizer = HuggingFaceTokenizer(
    tokenizer=AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
)

print(tokenizer.count_tokens("Hello world!"))  # 5
print(tokenizer.count_tokens_left("Hello world!"))  # 507
```

### Bedrock

#### Claude
```python
from griptape.tokenizers import BedrockClaudeTokenizer


tokenizer = BedrockClaudeTokenizer(model=BedrockClaudeTokenizer.DEFAULT_MODEL)

print(tokenizer.count_tokens("Hello world!")) # 2
print(tokenizer.count_tokens_left("Hello world!")) # 4094
```

#### Titan
```python
from griptape.tokenizers import BedrockTitanTokenizer


tokenizer = BedrockTitanTokenizer(model=BedrockTitanTokenizer.DEFAULT_MODEL)

print(tokenizer.count_tokens("Hello world!"))  # 5
print(tokenizer.count_tokens_left("Hello world!"))  # 4091
```

#### Jurassic
```python
from griptape.tokenizers import BedrockJurassicTokenizer


tokenizer = BedrockJurassicTokenizer(model=BedrockJurassicTokenizer.DEFAULT_MODEL)

print(tokenizer.count_tokens("Hello world!"))  # 3
print(tokenizer.count_tokens_left("Hello world!"))  # 8189
```


### Simple
Not all LLM providers have a public tokenizer API. In this case, you can use the `SimpleTokenizer` to count tokens based on a simple heuristic. 

```python
from griptape.tokenizers import SimpleTokenizer

tokenizer = SimpleTokenizer(max_tokens=1024, characters_per_token=6)

print(tokenizer.count_tokens("Hello world!")) # 2
print(tokenizer.count_tokens_left("Hello world!")) # 1022
```
