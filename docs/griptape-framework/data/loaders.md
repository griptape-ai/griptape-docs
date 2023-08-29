Loaders are used to load textual data from different sources and chunk it into `TextArtifact`s. Each loader can be used to load a single "document" with `load()` or multiple documents with `'load_collection()`.

## PdfLoader

Inherits from the `TextLoader` and can be used to load PDFs from a path or from an IO stream:

```python
from griptape.loaders import PdfLoader

PdfLoader().load(
    "path/to/file.pdf"
)

PdfLoader().load_collection(["path/to/file_1.pdf", "path/to/file_2.pdf"])
```

## SqlLoader

Can be used to load data from a SQL database into `CsvRowArtifact`s:

```python
from griptape.loaders import SqlLoader
from griptape.drivers import SqlDriver

SqlLoader(
    sql_driver=SqlDriver(engine_url="..."),
).load("SELECT * FROM users;")

SqlLoader(
    sql_driver=SqlDriver(engine_url="..."),
).load_collection(["SELECT * FROM users;", "SELECT * FROM products;"])
```

## TextLoader

Used to load arbitrary text and text files:

```python
from pathlib import Path
from griptape.loaders import TextLoader

TextLoader().load(
    "my text"
)

TextLoader().load(
    Path("path/to/file.txt")
)

TextLoader().load_collection(
    ["my text", "my other text", Path("path/to/file.txt")]
)
```

You can set a custom `tokenizer`, `max_tokens` parameter, `chunker`, and `embedding_driver`.

## WebLoader

Inherits from the `TextLoader` and can be used to load web pages:

```python
from griptape.loaders import WebLoader

WebLoader().load(
    "https://www.griptape.ai"
)

WebLoader().load_collection(
    ["https://www.griptape.ai", "https://docs.griptape.ai"]
)
```
