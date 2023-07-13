This example demonstrates how to build an agent that can dynamically query Amazon Redshift Serverless tables and store its contents on the local hard drive.

Let's build a support agent that uses GPT-4:

```python
import boto3
from griptape.drivers import AmazonRedshiftSqlDriver, OpenAiPromptDriver
from griptape.engines import VectorQueryEngine
from griptape.loaders import SqlLoader
from griptape.memory.tool import TextToolMemory
from griptape.rules import Ruleset, Rule
from griptape.structures import Agent
from griptape.tools import SqlClient, FileManager, TextMemoryBrowser
from griptape.utils import Chat

prompt_driver = OpenAiPromptDriver(
    model="gpt-4"
)

session = boto3.Session(region_name="REGION_NAME")

sql_loader = SqlLoader(
    sql_driver=AmazonRedshiftSqlDriver(
        database="DATABASE",
        session=session,
        workgroup_name="WORKGROUP_NAME"
    )
)

text_memory = TextToolMemory(
    query_engine=VectorQueryEngine(
        prompt_driver=prompt_driver
    )
)

file_manager_tool = FileManager(
    input_memory=[text_memory]
)

memory_browser_tool = TextMemoryBrowser(
    input_memory=[text_memory]
)

sql_tool = SqlClient(
    sql_loader=sql_loader,
    table_name="people",
    table_description="contains information about tech industry professionals",
    engine_name="redshift",
    output_memory={
        "execute_query": [text_memory]
    }
)

agent = Agent(
    prompt_driver=prompt_driver,
    tools=[sql_tool, file_manager_tool, memory_browser_tool],
    rulesets=[
        Ruleset(
            name="HumansOrg Agent",
            rules=[
                Rule("Act and introduce yourself as a HumansOrg, Inc. support agent"),
                Rule("Your main objective is to help with finding information about people"),
                Rule("Only use information about people from the sources available to you")
            ]
        )
    ]
)

Chat(agent).start()
```
