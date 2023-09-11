# Contributing

We appreciate contributions and help maintaining this repository.

## Report and Issue
The easiest way to contribute to our docs is through our public [issue tracker](https://github.com/griptape-ai/griptape-docs/issues). Feel free to submit bugs, request features or changes, or contribute to the project directly. 

## Pull Requests

Griptape docs are built using [MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/). Dependencies are managed using [Poetry](https://python-poetry.org/).

To directly contribute to Griptape documentation, first fork the [griptape-docs](https://github.com/griptape-ai/griptape-docs) repository to your GitHub account. Then clone your repository to your local machine.

From inside the directory run: 

```poetry install --with docs```

To run `griptape-docs` locally run: 

```peotry run mkdocs serve```

You should see something similar to the following: 

```
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.19 seconds
INFO     -  [09:28:33] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [09:28:33] Serving on http://127.0.0.1:8000/
INFO     -  [09:28:37] Browser connected: http://127.0.0.1:8000/
```

You may see many `WARNING` messages in the console output. This is because the [reference docs](./reference/griptape/index.md) are not built.
Fixing this is not necessary to contribute to the documentation, but it helps to reduce noise in the console output.

First, clone the Griptape repository to a separate directory:

`git clone git@github.com:griptape-ai/griptape.git ~/some/other/directory/`

Then, create a symlink called `griptape` in the `griptape-docs` repository:

`ln -s ~/some/other/directory/griptape griptape`

The `WARNING` messages should now be resolved. 


Follow the typical PR process to contribute changes. 

* Create a feature branch.
* Commit changes.
* Submit a PR.
