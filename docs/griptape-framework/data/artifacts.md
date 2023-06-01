**Artifacts** are used for passing different types of data between Griptape components. All tools return artifacts that are later consumed by tasks and ramps. Artifacts make sure framework components enforce contracts when passing and consuming data.

## TextArtifact

Used for passing text data of arbitrary size around the framework. It can be used to count tokens with `token_count()` with a tokenizer. It can also be used to generate a text embedding with `generate_embedding()` and access it with `embedding`.

`TextStorageRamp` automatically stores `TextArtifact`s returned by tool activities and returns artifact IDs back to the LLM.

## InfoArtifact

Used for passing short notifications back to the LLM without ramps modifying them.

## ErrorArtifact

Used for passing errors back to the LLM without ramps modifying them.

## BlobArtifact

Used for passing binary large objects (blobs) back to the LLM. Treat it as a way to return unstructured data, such as images, videos, audio, and other files back from tools. Each blob has a `name` and ` dir` to uniquely identify stored objects.

`BlobStorageRamp` automatically stores `BlobArtifact`s returned by tool activities that can be reused by other tools.

## ListArtifact

Used for storing multiple other artifacts in a list. Useful when tools need to return multiple objects.