To store your conversation on DynamoDB you can use DynamoDbConversationMemoryDriver.
```python
import os
import uuid
from griptape.drivers import DynamoDbConversationMemoryDriver
from griptape.memory.structure import ConversationMemory
from griptape.structures import Agent

conversation_id = uuid.uuid4().hex
dynamodb_driver = DynamoDbConversationMemoryDriver(
    table_name=os.environ["DYNAMODB_TABLE_NAME"],
    partition_key="id",
    value_attribute_key="memory",
    partition_key_value=conversation_id,
)

agent = Agent(memory=ConversationMemory(driver=dynamodb_driver))

agent.run("My name is Jeff.")
agent.run("What is my name?")

```
