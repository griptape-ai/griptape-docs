# Computer

This tool enables LLMs to execute Python code and run shell commands inside a Docker container. You have to have the Docker daemon running in order for this tool to work.

You can specify a local working directory and environment variables during tool initialization:

```python
Computer(
    local_workdir=os.path.abspath(os.path.join(os.getcwd(), "workdir")),
    env_vars={
        "ENV_VAR_1": "foo",
        "ENV_VAR_2": "bar",
    }
)
```