### Configuring the Griptape CLI

The Griptape CLI needs to be configured after installation. From the terminal window, run the following command: 

```shell
gt cloud configure
```

You'll be asked a series of configuration questions. 

| Question                               | Description                                                                                                                                                            |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Enter your Griptape Cloud API key:`   | Enter your Griptape Cloud API Key.                                                                                                                                     |
| `Select the endpoint you want to use:` | If you're part of the Private Preview, select __other__ and enter `https://api.cloud-preview.griptape.ai`. Leave the default for Griptape Cloud's production endpoint. |
| `Select the organization you want to use:`                               | Leave the default or select an alternate organization.                                                                                                                 |
| `Select the environment you want to use: ` | Leave the default or select an alternate environment. |
| 'Enter a name for this profile [default]: | Leave the default. We suggest changing this to `preview` or something equivalent if you're part of the Private Preview. |