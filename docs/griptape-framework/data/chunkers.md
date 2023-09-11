## Overview

Chunkers are used to split arbitrarily long text into chunks of certain token length. 
Each chunker has a tokenizer, a max token count, and a list of default separators used to split up text into [TextArtifact](../../reference/griptape/artifacts/text_artifact.md)s. 
Different types of chunkers provide lists of separators for specific text shapes:

* [TextChunker](../../reference/griptape/chunkers/text_chunker.md): works on most texts.
* [PdfChunker](../../reference/griptape/chunkers/pdf_chunker.md): works on text from PDF docs.
* [MarkdownChunker](../../reference/griptape/chunkers/markdown_chunker.md) works on markdown text.

Here is how to use a chunker:

```python
>>> from griptape.chunkers import TextChunker
>>> from griptape.tokenizers import TiktokenTokenizer
>>> TextChunker(
...     # set an optional custom tokenizer
...     tokenizer=TiktokenTokenizer(),
...     # optionally modify default number of tokens
...     max_tokens=100
... ).chunk("long text")
[TextArtifact(id='...', name='...', type='TextArtifact', value='long text', _TextArtifact__embedding=[])]

```
