Loaders are used to load textual data from different sources and chunk it into `TextArtifact`s. Each loader can be used to load a single "document" with `load()` or multiple documents with `'load_collection()`.

## PdfLoader

Inherits from the `TextLoader` and can be used to load PDFs from a path or from an IO stream:

```python
PdfLoader().load(
    "path/to/file.pdf"
)

PdfLoader().load_collection(
    "path/to/file_1.pdf",
    "path/to/file_2.pdf"
)
```

## SqlLoader

Can be used to load data from a SQL database into `CsvRowArtifact`s:

```python
SqlLoader().load(
    sql_driver=SqlDriver(
        engine_url="..."
    ),
    "SELECT * FROM users;"
)

SqlLoader().load_collection(
    sql_driver=SqlDriver(
        engine_url="..."
    ),
    "SELECT * FROM users;",
    "SELECT * FROM products;"
)
```

## TextLoader

Used to load arbitrary text:

```python
TextLoader().load(
    "my text"
)

TextLoader().load_collection(
    "my text",
    "my other text"
)
```

You can set a custom `tokenizer`, `max_tokens` parameter, `chunker`, and `embedding_driver`.

## WebLoader

Inherits from the `TextLoader` and can be used to load web pages:

```python
WebLoader().load(
    "https://www.griptape.ai"
)

WebLoader().load_collection(
    "https://www.griptape.ai",
    "https://docs.griptape.ai"
)
```