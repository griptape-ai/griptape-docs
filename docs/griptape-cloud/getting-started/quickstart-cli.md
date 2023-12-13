# Getting Started 

Before you can create your first application using the Griptape CLI, make sure you have completed the [Installation](../cli/index.md) steps for the Griptape CLI. 

First, you need to make sure your CLI is configured to your Griptape Cloud environment. Run `gt cloud configure` from your Terminal application. You will be asked to select an _organization_ and an _environment_. Finally, you'll be asked to name this profile. Below, I left the default (_default_).

1. __gt cloud configure__

```shell
user@machine-name ~ % gt cloud configure
? Select the organization you want to use: 
1). default: 5f01a7b7-4d3a-441e-ac92-9ee74h8d28ea
? Select the environment you want to use: 
1). default: e9faefbd-fea0-44b8-b4e7-95f728bdbd9f
Enter a name for this profile [default]:
Successfully configured profile default!
```

2. __gt cloud list-organizations__ (optional step for validation)

The `list-organizations` command list the __organizations__ you have in your Griptape Cloud account. For Private Preview users, you should only see one entry. 
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

You should see something like the following. In this example, I'm creating an app called _demo_app_ in my Home directory. I'm then verifying it's contents via `ls`. 

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