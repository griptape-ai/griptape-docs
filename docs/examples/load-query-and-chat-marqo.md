```python
import os
from griptape import utils
from griptape.drivers import MarqoVectorStoreDriver
from griptape.engines import VectorQueryEngine
from griptape.loaders import WebLoader
from griptape.structures import Agent
from griptape.tools import VectorStoreClient

# Define the namespace
namespace = "griptape-ai"

# Initialize the vector store driver
vector_store = MarqoVectorStoreDriver(
    api_key=os.environ["MARQO_API_KEY"],
    url=os.environ["MARQO_URL"],
    index=os.environ["MARQO_INDEX_NAME"],
)

# Initialize the query engine
query_engine = VectorQueryEngine(vector_store_driver=vector_store)

# Initialize the knowledge base tool
vector_store_tool = VectorStoreClient(
    description="Contains information about the Griptape Framework from www.griptape.ai",
    query_engine=query_engine,
    namespace=namespace,
)

# Load artifacts from the web
artifacts = WebLoader(max_tokens=200).load("https://www.griptape.ai")

# Upsert the artifacts into the vector store
vector_store.upsert_text_artifacts(
    {
        namespace: artifacts,
    }
)

# Initialize the agent
agent = Agent(tools=[vector_store_tool])

# Start the chat
utils.Chat(agent).start()
```
