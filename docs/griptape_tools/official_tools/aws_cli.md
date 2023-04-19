# AwsCli

This tool enables LLMs to run AWS CLI commands. Before using this tool, make sure to [install and configure](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) AWS CLI v2.

```python
AwsCli(
    aws_access_key_id=config("aws_access_key_id"),
    aws_secret_access_key=config("aws_secret_access_key"),
    aws_cli_policy="""{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"*","Resource":"*"}]}"""
)
```
