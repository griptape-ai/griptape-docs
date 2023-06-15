SQL drivers can be used to make SQL queries and load table schemas. They are used by the `SqlLoader` to process data. All loaders implement the following methods:

* `execute_query()` executes a query and returns `RowResult`s.
* `execute_query_row()` executes a query and returns a raw result from SQL.
* `get_table_schema()` returns a table schema.

!!! info
    More database-specific SQL drivers are coming soon.

## SqlDriver

This is a basic SQL loader based on [SQLAlchemy 1.x](https://docs.sqlalchemy.org/en/14/). Here is an example of how to use it:

```python
driver = SqlDriver(
    engine_url="sqlite:///:memory:"
)

driver.execute_query("select * from users;")
```