# Installing the Griptape CLI

Installing the Griptape CLI is simple. Follow these steps to install using [pipx](https://github.com/pypa/pipx).

1. Install pipx if you haven't already.

```sh
python3 -m pip install --user pipx
```

2. Use pipx to install the Griptape CLI Package.

```sh
python3 -m pipx install griptape-cli
```

3. Verify your installation

```sh
gt --help
```

### Configuring the Griptape CLI

**API KEY**

Currently, the Griptape CLI looks for an environment variable named `GRIPTAPE_CLOUD_API_KEY`. You can set this variable in whatever way you find most convenient. We plan to remove this requirement in place of a configuration option, but it's required in the current version.

```sh
export GRIPTAPE_CLOUD_API_KEY=<api_key>
```

**CLOUD ENDPOINT**

Griptape has multiple cloud endpoints. In some cases, such as the Private Preview, we are using a specific environment to isolate users. The CLI currently looks for an environment variable named `GRIPTAPE_CLOUD_ENDPOINT_URL` and uses that for all CLI commands.

If you're using Griptape in Production, you can skip this step and the CLI will default to the production environment. For Private Preview users, set the following in your environment.

```sh
export GRIPTAPE_CLOUD_ENDPOINT_URL="https://cloud-preview.griptape.ai"
```
