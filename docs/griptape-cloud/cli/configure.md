### Configuring the Griptape CLI

The Griptape CLI needs to be configured after installation. From the terminal window, run the following command:

```shell
gt cloud configure
```

You'll be asked a series of configuration questions.

| Question                                   | Description                                                                                                                                                                                          |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Enter your Griptape Cloud API key:`       | Enter your Griptape Cloud API Key.                                                                                                                                                                   |
| `Select the endpoint you want to use:`     | If you're part of the Private Preview, select `https://api.cloud-preview.griptape.ai`. Select **Other** to target additional Griptape Cloud endpoints.                                               |
| `Select the organization you want to use:` | Leave the default or select an alternate organization.                                                                                                                                               |
| `Select the environment you want to use: ` | Leave the default or select an alternate environment.                                                                                                                                                |
| 'Enter a name for this profile [default]:  | Leave the default to have the CLI use this profile by default. It is possible to configure multiple named profiles, such as `preview` or something equivalent if you're part of the Private Preview. |
