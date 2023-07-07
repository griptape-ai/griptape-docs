This example demonstrates how to build an agent that can dynamically query AWS Redshift tables and store its contents on the local hard drive.

Before running this example, make sure to install the following dependencies, so that the `SqlDriver` works correctly with Redshift:

```shell
pip install sqlalchemy~="1.0"
pip install sqlalchemy-redshift

# Before installing psycopg2, install postgresql-devel in your system.
# For example, `sudo yum install postgresql-devel`.
pip install psycopg2
pip install psycopg2-binary
pip install redshift_connector
```

Now, let's build a support agent that uses GPT-4:

```python
from decouple import config
from griptape.drivers import SqlDriver, OpenAiPromptDriver
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

sql_loader = SqlLoader(
    sql_driver=SqlDriver(
        engine_url=config("REDSHIFT_URL")
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
