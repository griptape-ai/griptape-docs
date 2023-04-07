# Griptape Docs
The documentation for Griptape, and Skatepark are actively maintained and constantly improving projects. We appreciate contributions and help maintaining the repository. 

## Reporting an issue with Griptape Docs
The easiest way to contribute to our docs is through our public [issue tracker](https://github.com/griptape-ai/griptape-docs/issues). Feel free to submit bugs, request features or changes, or contribute to the project directly. 

## Contributing directly to griptape-docs through a PR 
To directly contribute to Griptape's documentation, first fork the [griptape-docs](https://github.com/griptape-ai/griptape-docs) repository to your github account. Then clone your repository to your local machine. Griptape docs are built using [MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/). 

From inside the directory, run: 

`% pip install -r docs/requirements.txt`

To run griptape-docs locally, run: 

`% mkdocs serve`

You should see something similar to the following: 

```
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.19 seconds
INFO     -  [09:28:33] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [09:28:33] Serving on http://127.0.0.1:8000/
INFO     -  [09:28:37] Browser connected: http://127.0.0.1:8000/
```

Follow the typical PR process to contribute changes. 

- create a feature branch
- commmit changes
- submit PR