## Overview

Loaders are used to load textual data from different sources and chunk it into [TextArtifact](../../reference/griptape/artifacts/text_artifact.md)s.
Each loader can be used to load a single "document" with [load()](../../reference/griptape/loaders/base_loader.md#griptape.loaders.base_loader.BaseLoader.load) or
multiple documents with ['load_collection()](../../reference/griptape/loaders/base_loader.md#griptape.loaders.base_loader.BaseLoader.load_collection).

## PdfLoader

Inherits from the [TextLoader](../../reference/griptape/loaders/text_loader.md) and can be used to load PDFs from a path or from an IO stream:

```python
>>> from griptape.loaders import PdfLoader
>>> import urllib.request

>>> urllib.request.urlretrieve("https://arxiv.org/pdf/1706.03762.pdf", "attention.pdf")
('attention.pdf', <http.client.HTTPMessage object at ...>)

>>> PdfLoader().load("attention.pdf")
[TextArtifact(id='...', name='...', type='TextArtifact', value='...', _TextArtifact__embedding=[])]

>>> urllib.request.urlretrieve("https://arxiv.org/pdf/1706.03762.pdf", "CoT.pdf")
('CoT.pdf', <http.client.HTTPMessage object at ...>)

>>> PdfLoader().load_collection(["attention.pdf", "CoT.pdf"])
{'...': [TextArtifact(id='...', name='...', type='TextArtifact', value='...', _TextArtifact__embedding=[])], '...': [TextArtifact(id='...', name='...', type='TextArtifact', value='...', _TextArtifact__embedding=[])]}

```

## SqlLoader

Can be used to load data from a SQL database into [CsvRowArtifact](../../reference/griptape/artifacts/csv_row_artifact.md)s:

```python
>>> from griptape.loaders import SqlLoader
>>> from griptape.drivers import SqlDriver

>>> SqlLoader(
...     sql_driver = SqlDriver(
...        engine_url="sqlite:///:memory:"
...     )
... ).load("SELECT 'foo', 'bar'")
[CsvRowArtifact(id='...', name='...', type='CsvRowArtifact', _TextArtifact__embedding=[], value={"'foo'": 'foo', "'bar'": 'bar'}, delimiter=',')]

>>> SqlLoader(
...    sql_driver = SqlDriver(
...        engine_url="sqlite:///:memory:"
...    )
... ).load_collection(["SELECT 'foo', 'bar';", "SELECT 'fizz', 'buzz';"])
{'...': [CsvRowArtifact(id='...', name='...', type='CsvRowArtifact', _TextArtifact__embedding=[], value={"'foo'": 'foo', "'bar'": 'bar'}, delimiter=',')], '...': [CsvRowArtifact(id='...', name='...', type='CsvRowArtifact', _TextArtifact__embedding=[], value={"'fizz'": 'fizz', "'buzz'": 'buzz'}, delimiter=',')]}

```

## CsvLoader

Can be used to load CSV files into [CsvRowArtifact](../../reference/griptape/artifacts/csv_row_artifact.md)s:

```python
>>> import urllib
>>> from griptape.loaders import CsvLoader

>>> urllib.request.urlretrieve("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv", "cities.csv")
('cities.csv', <http.client.HTTPMessage object at ...>)

>>> CsvLoader().load(
...    "cities.csv"
... )
[CsvRowArtifact(id='...', name='...', type='CsvRowArtifact', _TextArtifact__embedding=[], value={...}, delimiter=','), ...]

>>> urllib.request.urlretrieve("https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv", "addresses.csv")
('addresses.csv', <http.client.HTTPMessage object at ...>)

>>> CsvLoader().load_collection(
...     ["cities.csv", "addresses.csv"]
... )
{'...': [CsvRowArtifact(id='...', name='...', type='CsvRowArtifact', _TextArtifact__embedding=[], value={...}, delimiter=','), ...], '...': [CsvRowArtifact(id='...', name='...', type='CsvRowArtifact', _TextArtifact__embedding=[], value={...}, delimiter=','), ...]}
 
```

## TextLoader

Used to load arbitrary text and text files:

```python
>>> from pathlib import Path
>>> import urllib
>>> from griptape.loaders import TextLoader

>>> TextLoader().load(
...    "my text"
... )
[TextArtifact(id='...', name='...', type='TextArtifact', value='my text', _TextArtifact__embedding=[])]

>>> urllib.request.urlretrieve("https://example-files.online-convert.com/document/txt/example.txt", "example.txt")
('example.txt', <http.client.HTTPMessage object at ...>)

>>> TextLoader().load(
...    Path("example.txt")
... )
[TextArtifact(id='...', name='...', type='TextArtifact', value='...', _TextArtifact__embedding=[])]

>>> TextLoader().load_collection(
...     ["my text", "my other text", Path("example.txt")]
... )
{'...': [TextArtifact(id='...', name='...', type='TextArtifact', value='my text', _TextArtifact__embedding=[])], '...': [TextArtifact(id='...', name='...', type='TextArtifact', value='my other text', _TextArtifact__embedding=[])], '...': [TextArtifact(id='...', name='...', type='TextArtifact', value='...', _TextArtifact__embedding=[])]}
    
```

You can set a custom [tokenizer](../../reference/griptape/loaders/text_loader.md#griptape.loaders.text_loader.TextLoader.tokenizer.md), [max_tokens](../../reference/griptape/loaders/text_loader.md#griptape.loaders.text_loader.TextLoader.max_tokens.md) parameter, and [chunker](../../reference/griptape/loaders/text_loader.md#griptape.loaders.text_loader.TextLoader.chunker.md).

## WebLoader

Inherits from the [TextLoader](../../reference/griptape/loaders/text_loader.md) and can be used to load web pages:

```python
>>> from griptape.loaders import WebLoader

>>> WebLoader().load(
...     "https://www.griptape.ai"
... )
[TextArtifact(id='...', name='...', type='TextArtifact', value='...', _TextArtifact__embedding=[])]

>>> WebLoader().load_collection(
...    ["https://www.griptape.ai", "https://docs.griptape.ai"]
... )
{'...': [TextArtifact(id='...', name='...', type='TextArtifact', value='...', _TextArtifact__embedding=[])], '...': [TextArtifact(id='...', name='...', type='TextArtifact', value="...", _TextArtifact__embedding=[])]}

```
