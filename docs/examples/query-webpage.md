```python
from griptape.artifacts import BaseArtifact
from griptape.drivers import MemoryVectorDriver
from griptape.loaders import WebLoader


vector_driver = MemoryVectorDriver()
artifacts = WebLoader(max_tokens=100).load("https://www.griptape.ai")

[vector_driver.upsert_text_artifact(a, namespace="griptape") for a in artifacts]

results = vector_driver.query(
    "creativity",
    count=3,
    namespace="griptape"
)

values = [BaseArtifact.from_json(r.meta["artifact"]).value for r in results]

print("\n\n".join(values))

```