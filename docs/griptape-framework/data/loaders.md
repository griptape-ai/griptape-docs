## Overview

Loaders are used to load textual data from different sources and chunk it into [TextArtifact](../../reference/griptape/artifacts/text_artifact.md)s.
Each loader can be used to load a single "document" with [load()](../../reference/griptape/loaders/base_loader.md#griptape.loaders.base_loader.BaseLoader.load) or
multiple documents with [load_collection()](../../reference/griptape/loaders/base_loader.md#griptape.loaders.base_loader.BaseLoader.load_collection).

## Pdf Loader

Inherits from the [TextLoader](../../reference/griptape/loaders/text_loader.md) and can be used to load PDFs from a path or from an IO stream:

```python
from griptape.loaders import PdfLoader
import urllib.request

urllib.request.urlretrieve("https://arxiv.org/pdf/1706.03762.pdf", "attention.pdf")

PdfLoader().load("attention.pdf")

urllib.request.urlretrieve("https://arxiv.org/pdf/1706.03762.pdf", "CoT.pdf")

PdfLoader().load_collection(["attention.pdf", "CoT.pdf"])
```

## Sql Loader

Can be used to load data from a SQL database into [CsvRowArtifact](../../reference/griptape/artifacts/csv_row_artifact.md)s:

```python
from griptape.loaders import SqlLoader
from griptape.drivers import SqlDriver

SqlLoader(
    sql_driver = SqlDriver(
        engine_url="sqlite:///:memory:"
    )
).load("SELECT 'foo', 'bar'")

SqlLoader(
    sql_driver = SqlDriver(
        engine_url="sqlite:///:memory:"
    )
).load_collection(["SELECT 'foo', 'bar';", "SELECT 'fizz', 'buzz';"])
```

## Csv Loader

Can be used to load CSV files into [CsvRowArtifact](../../reference/griptape/artifacts/csv_row_artifact.md)s:

```python
import urllib
from griptape.loaders import CsvLoader

urllib.request.urlretrieve("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv", "cities.csv")

CsvLoader().load(
    "cities.csv"
)

urllib.request.urlretrieve("https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv", "addresses.csv")

CsvLoader().load_collection(
    ["cities.csv", "addresses.csv"]
)
```

## Text Loader

Used to load arbitrary text and text files:

```python
from pathlib import Path
import urllib
from griptape.loaders import TextLoader

TextLoader().load(
    "my text"
)

urllib.request.urlretrieve("https://example-files.online-convert.com/document/txt/example.txt", "example.txt")

TextLoader().load(
    Path("example.txt")
)

TextLoader().load_collection(
    ["my text", "my other text", Path("example.txt")]
)
```

You can set a custom [tokenizer](../../reference/griptape/loaders/text_loader.md#griptape.loaders.text_loader.TextLoader.tokenizer.md), [max_tokens](../../reference/griptape/loaders/text_loader.md#griptape.loaders.text_loader.TextLoader.max_tokens.md) parameter, and [chunker](../../reference/griptape/loaders/text_loader.md#griptape.loaders.text_loader.TextLoader.chunker.md).

## Web Loader

Inherits from the [TextLoader](../../reference/griptape/loaders/text_loader.md) and can be used to load web pages:

```python
from griptape.loaders import WebLoader

WebLoader().load(
    "https://www.griptape.ai"
)

WebLoader().load_collection(
    ["https://www.griptape.ai", "https://docs.griptape.ai"]
)
```

## Image Loader

The Image Loader is used to load an image from the filesystem, returning an ImageArtifact.

```python
from griptape.loaders import ImageLoader

image_artifact = ImageLoader().load("my_image.png")

image_artifacts = ImageLoader().load_collection("image_1.png", "image_2.png")
```

By default, the Image Loader will ensure all images are in `png` format. If an image in another format (for example, `jpg`) is loaded, it will be reformatted to `png`. Other formats are supported through the `format` field.

```python
from griptape.loaders import ImageLoader


# Image data in Image Artifact will be in JPG format
image_artifact_jpg = ImageLoader(format="JPG").load("my_image.png")
```
