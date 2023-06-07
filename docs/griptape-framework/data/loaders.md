Loaders are used to load textual data from different sources.

## TextLoader

Used to load arbitrary text:

```python
TextLoader().load("my text")
```

You can set custom `tokenizer`, `max_tokens`, `chunker`, and `embedding_driver`.

## WebLoader

Inherits from the `TextLoader` and can be used to load web pages:

```python
WebLoader().load("https://www.griptape.ai")
```

## PdfLoader

Inherits from the `TextLoader` and can be used to load PDFs from a path or from an IO stream:

```python
PdfLoader().load("path/to/file.pdf")
```