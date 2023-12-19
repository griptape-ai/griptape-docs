# Getting Started

Before you can create your first application using the Griptape CLI, make sure you have completed the [Installation](../cli/index.md) steps for the Griptape CLI.

Step 1. **gt cloud configure**

If you haven't already, you need to make sure your CLI is configured to your Griptape Cloud environment. You can read more about the configuration options and suggested default in [this guide](../cli/configure.md).

```shell
gt cloud configure
```

Step 2. **gt cloud list-organizations** (optional step for validation)

The `list-organizations` command lists the **organizations** you have in your Griptape Cloud account. For Private Preview users, you should only see one entry.

```shell
gt cloud list-organizations
```

```{: .optional-language-as-class .no-copy}
user@machine-name ~ % gt cloud list-organizations
{'organizations':
[{'created_at': '2023-11-21T21:42:19.147Z'
'created_by': 'f4dhcb95-3ad7-4941-868e-2bncjd2c83d1',
'name': 'default',
'organization_id': '5f01a7b7-4d3a-441e-ac92-9ee74h8d28ea',
'updated_at': '2023-11-21T21:42:19.147Z'}]
}
```

Step 3. **gt app new --directory ~/workplace demo_app**

Next, we can use the Griptape CLI to scaffold a sample project that is compatible with Griptape Cloud and has a default structure in place. This is a quick way to get started if you aren't converting an existing Python project to Griptape.

You should see something like the following. In this example, I'm creating an app called _demo_app_ in my Home directory. I'm then verifying its contents via `ls`.

```shell
gt app new --directory ~/demo_app
```

```{: .optional-language-as-class .no-copy}
user@machine-name ~ % gt app new --directory ~/demo_app
Initializing app demo_app
user@machine-name ~ % ls ~/demo_app
README.md		__pycache__		app.py			requirements.txt	tests
```

Step 4. Add your AI variables using a .env file.

Currently, in Private Preview, Griptape Cloud apps use .env files to store API Keys for services like OpenAI, Amazon Bedrock, Anthropic, Hugging Face.

```shell
user@machine-name ~ % cd ~/demo_app
user@machine-name demo_app % echo OPENAI_API_KEY="YOUR OPENAI KEY" > .env
```

Step 5. Test your application locally

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

Step 6. Create an app on the cloud

You can use the Griptape CLI to create an app on the cloud.

```
user@machine-name demo_app % gt cloud create-app --name "Demo App"
{'app_id': '12345678-8f3e-4028-9934-42e0cd69860a', 'created_at': '2023-12-19T00:14:09.021Z', 'created_by': '12345678-9b16-408a-b5d7-e83044d820f4', 'environment_id': '12345678-5cde-4075-beee-2612ba8e6011', 'name': 'Demo App', 'updated_at': '2023-12-19T00:14:09.021Z'}
```

Step 7. Deploy your application to the cloud

You can use the Griptape CLI to deploy your application to the cloud.

```
user@machine-name demo_app % gt cloud create-deployment --api-id 12345678-8f3e-4028-9934-42e0cd69860a --directory ~/demo_app
{'app_id': '12345678-8f3e-4028-9934-42e0cd69860a', 'created_at': '2023-12-19T00:16:36.663Z', 'created_by': '12345678-9b16-408a-b5d7-e83044d820f4', 'deployment_id': '12345678-12cd-4003-9ee1-b6b01f7927ea', 'status': 'QUEUED'}
```

Step 8. Run your application on the cloud

You can use the Griptape CLI to run your application on the cloud.

```
user@machine-name demo_app % gt cloud run --app-id 12345678-8f3e-4028-9934-42e0cd69860a --arg "write me a haiku about a skateboard?"
{'app_id': '1e6d77a7-8f3e-4028-9934-42e0cd69860a', 'created_at': '2023-12-19T00:22:38.559Z', 'created_by': '36531b12-9b16-408a-b5d7-e83044d820f4', 'deployment_id': '80d055f8-e311-4b5b-be0f-54d466ba1bd7', 'run_id': '5613df80-a83f-4b76-9e6d-237419787ff8', 'session_id': '9141d887-dcb2-4353-a20e-b384933ba5d0', 'status': 'QUEUED', 'args': ['write me a haiku about a skateboard?']}

Polling run and events...

{'contents': {'body': '{"timestamp": 1702945359.8019736, "type": "StartStructureRunEvent"}'}, 'event_id': '67546f6b-07d3-4f65-88eb-f2acfe60d704', 'run_id': '5613df80-a83f-4b76-9e6d-237419787ff8', 'timestamp': 1702945359801973, 'type': 'StartStructureRunEvent'}


{'contents': {'body': '{"timestamp": 1702945359.8957925, "type": "StartTaskEvent", "task_id": "e28e079b00cf43d79ba53fc2f5c496b1", "task_parent_ids": [], "task_child_ids": [], "task_input": {"id": "07ac8dcce0ee48138e314eca461bd69e", "name": "07ac8dcce0ee48138e314eca461bd69e", "type": "TextArtifact", "value": "write me a haiku about a skateboard?"}, "task_output": null}'}, 'event_id': 'b8ff1f4d-90df-41ac-8031-47508930a256', 'run_id': '5613df80-a83f-4b76-9e6d-237419787ff8', 'timestamp': 1702945359895792, 'type': 'StartTaskEvent'}


{'contents': {'body': '{"timestamp": 1702945361.2497554, "type": "StartPromptEvent", "token_count": 20, "prompt_stack": {"inputs": [{"content": "", "role": "system"}, {"content": "write me a haiku about a skateboard?", "role": "user"}]}, "prompt": "\\n\\nUser: write me a haiku about a skateboard?\\n\\nAssistant:"}'}, 'event_id': '539f7eaf-9ae3-4526-9c57-33bb90bca9da', 'run_id': '5613df80-a83f-4b76-9e6d-237419787ff8', 'timestamp': 1702945361249755, 'type': 'StartPromptEvent'}


{'contents': {'body': '{"timestamp": 1702945366.6903105, "type": "FinishPromptEvent", "token_count": 20, "result": "Wheels glide on pavement,\\nFreedom beneath the sun\'s gaze,\\nSkateboard, my escape."}'}, 'event_id': '260f4530-1f55-4ae1-975e-90bd8539afdd', 'run_id': '5613df80-a83f-4b76-9e6d-237419787ff8', 'timestamp': 1702945366690310, 'type': 'FinishPromptEvent'}


{'contents': {'body': '{"timestamp": 1702945366.7016082, "type": "FinishTaskEvent", "task_id": "e28e079b00cf43d79ba53fc2f5c496b1", "task_parent_ids": [], "task_child_ids": [], "task_input": {"id": "382bf9e4a2a44c0bb3311fe794ecc163", "name": "382bf9e4a2a44c0bb3311fe794ecc163", "type": "TextArtifact", "value": "write me a haiku about a skateboard?"}, "task_output": {"id": "27ed74fd1a324f1b9ca129898c2dbc6b", "name": "27ed74fd1a324f1b9ca129898c2dbc6b", "type": "TextArtifact", "value": "Wheels glide on pavement,\\nFreedom beneath the sun\'s gaze,\\nSkateboard, my escape."}}'}, 'event_id': '67488767-211c-4127-ba9c-67563b6646a0', 'run_id': '5613df80-a83f-4b76-9e6d-237419787ff8', 'timestamp': 1702945366701608, 'type': 'FinishTaskEvent'}


{'contents': {'body': '{"timestamp": 1702945366.8563282, "type": "FinishStructureRunEvent"}'}, 'event_id': '9e4ac45a-2e8c-4ab5-925a-fd5d1617caea', 'run_id': '5613df80-a83f-4b76-9e6d-237419787ff8', 'timestamp': 1702945366856328, 'type': 'FinishStructureRunEvent'}


{'name': '27ed74fd1a324f1b9ca129898c2dbc6b', 'id': '27ed74fd1a324f1b9ca129898c2dbc6b', 'type': 'TextArtifact', 'value': "Wheels glide on pavement,\nFreedom beneath the sun's gaze,\nSkateboard, my escape."}
```
