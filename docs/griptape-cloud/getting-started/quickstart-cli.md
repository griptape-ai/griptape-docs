# Getting Started 

Before you can create your first application using the Griptape CLI, make sure you have completed the [Installation](../cli/index.md) steps for the Griptape CLI. 

1. __gt cloud configure__

If you haven't already, you need to make sure your CLI is configured to your Griptape Cloud environment. You can read more about the configuration options and suggested default in [this guide](../cli/configure.md). 

```shell
gt cloud configure
```

2. __gt cloud list-organizations__ (optional step for validation)

The `list-organizations` command lists the __organizations__ you have in your Griptape Cloud account. For Private Preview users, you should only see one entry. 
```shell
user@machine-name ~ % gt cloud list-organizations
{'organizations': 
[{'created_at': '2023-11-21T21:42:19.147Z'
'created_by': 'f4dhcb95-3ad7-4941-868e-2bncjd2c83d1', 
'name': 'default', 
'organization_id': '5f01a7b7-4d3a-441e-ac92-9ee74h8d28ea', 
'updated_at': '2023-11-21T21:42:19.147Z'}]
}
```

3. __gt app new --directory ~/workplace demo_app__

Next, we can use the Griptape CLI to scaffold a sample project that is compatible with Griptape Cloud and has a default structure in place. This is a quick way to get started if you aren't converting an existing Python project to Griptape.

You should see something like the following. In this example, I'm creating an app called _demo_app_ in my Home directory. I'm then verifying its contents via `ls`. 

```shell
user@machine-name ~ % gt app new --directory ~/ demo_app
Initializing app demo_app
user@machine-name ~ % ls ~/demo_app
README.md		__pycache__		app.py			requirements.txt	tests
```

4. Add your AI variables using a .env file. 

Currently, in Private Preview, Griptape Cloud apps use .env files to store API Keys for services like OpenAI, Amazon Bedrock, Anthropic, Hugging Face.

```shell
user@machine-name ~ % cd ~/demo_app
user@machine-name demo_app % echo OPENAI_API_KEY="YOUR OPENAI KEY" > .env
``` 

5. Test your application locally

You can use the Griptape CLI to run your application locally. The default project uses OpenAI, so this will require a valid OPENAI_API_KEY variable in a .env file in your project (step 4). 

```
user@machine-name demo_app % gt app run --directory ~/demo_app --arg "write me a haiku about a skateboard?"
Running app

[ installation of required packages if necessary ]

Installing collected packages: python-dotenv
Successfully installed python-dotenv-1.0.0
[12/12/23 20:33:49] INFO     PromptTask cecaba17b86746e4966a6ae4afbb3b4d
                             Input: write me a haiku about a skateboard?
[12/12/23 20:33:52] INFO     PromptTask cecaba17b86746e4966a6ae4afbb3b4d
                             Output: Wheels glide on pavement,
                             Freedom beneath the sun's gaze,
                             Skateboard, my escape.
```
