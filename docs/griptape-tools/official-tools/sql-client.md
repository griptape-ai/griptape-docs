# SqlClient

This tool enables LLMs to execute SQL statements via [SQLAlchemy](https://www.sqlalchemy.org/). Depending on your underlying SQL engine, [configure](https://docs.sqlalchemy.org/en/20/core/engines.html) your `engine_url` and give the LLM a hint about what engine you are using via `engine_name`, so that it can create engine-specific statements.

```python
from griptape.tools import SqlClient
from griptape.loaders import SqlLoader
from griptape.drivers import SqlDriver

client = SqlClient(
    table_name="users",
    sql_loader=SqlLoader(sql_driver=SqlDriver(engine_url="sqlite:///:memory:")),
)
```
