# SqlClient

This tool enables LLMs to execute SQL statements via [SQLAlchemy](https://www.sqlalchemy.org/). Depending on your underlying SQL engine, [configure](https://docs.sqlalchemy.org/en/20/core/engines.html) your `engine_url` and give the LLM a hint about what engine you are using via `engine_name`, so that it can create engine-specific statements.

```python
from griptape.tools import SqlClient
from griptape.structures import Agent
from griptape.loaders import SqlLoader

# Define the SqlLoader. This is just a basic example, and in practice, you'd initialize it based on your DBMS.
sql_loader = SqlLoader(driver_name="YOUR_DB_DRIVER", connection_string="YOUR_CONNECTION_STRING")

# Create the SqlClient tool
sql_tool = SqlClient(
    sql_loader=sql_loader,
    table_name="YOUR_TABLE_NAME",  # replace with your table name
    schema_name="YOUR_SCHEMA_NAME",  # replace with your schema name if you have one, else remove this line
    engine_name="YOUR_ENGINE_NAME",  # e.g., 'postgres', 'mysql', etc.
    table_description="Description of your table"  # replace with your table description or remove if not necessary
)

# Set up an agent using the SqlClient tool
agent = Agent(
    tools=[sql_tool]
)

# Task: Execute an SQL query
query_result = agent.run({
    "description": "Execute SQL query",
    "tool": "SqlClient",
    "activity": "execute_query",
    "values": {
        "sql_query": "SELECT * FROM YOUR_TABLE_NAME WHERE YOUR_CONDITION"  # replace with your actual SQL query
    }
})

if isinstance(query_result, InfoArtifact):
    print(f"Message: {query_result}")
else:
    for row in query_result:
        print(row.data)  # or however you wish to process each CsvRowArtifact
```
