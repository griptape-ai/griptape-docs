SQL drivers can be used to make SQL queries and load table schemas. They are used by the `SqlLoader` to process data. All loaders implement the following methods:

* `execute_query()` executes a query and returns `RowResult`s.
* `execute_query_row()` executes a query and returns a raw result from SQL.
* `get_table_schema()` returns a table schema.

!!! info
    More database-specific SQL drivers are coming soon.

## SqlDriver

This is a basic SQL loader based on [SQLAlchemy 1.x](https://docs.sqlalchemy.org/en/14/). Here is an example of how to use it:

```python
from griptape.drivers import SqlDriver

driver = SqlDriver(
    engine_url="sqlite:///:memory:"
)

driver.execute_query("select * from users;")
```

## AmazonRedshiftSqlDriver

This is a SQL driver for interacting with the [Amazon Redshift Data API](https://docs.aws.amazon.com/redshift-data/latest/APIReference/Welcome.html) 
to execute statements. Here is an example of how to use it for Redshift Serverless:

```python
import boto3
import os
from griptape.drivers import AmazonRedshiftSqlDriver

session = boto3.Session(region_name=os.getenv('AWS_DEFAULT_REGION'))

driver = AmazonRedshiftSqlDriver(
    database=os.getenv("REDSHIFT_DATABASE"),
    session=session,
    cluster_identifier=os.getenv('REDSHIFT_CLUSTER_IDENTIFIER'),
)

driver.execute_query("select * from people;")
```

## SnowflakeSqlDriver

This is a SQL driver based on the [Snowflake SQLAlchemy Toolkit](https://docs.snowflake.com/en/developer-guide/python-connector/sqlalchemy) which runs on top of the Snowflake Connector for Python. Here is an example of how to use it:

```python
import os
import snowflake.connector
from snowflake.connector import SnowflakeConnection
from griptape.drivers import SnowflakeSqlDriver

def get_snowflake_connection() -> SnowflakeConnection:
    return snowflake.connector.connect(
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE')
    )

driver = SnowflakeSqlDriver(connection_func=get_snowflake_connection)

driver.execute_query("select * from people;")