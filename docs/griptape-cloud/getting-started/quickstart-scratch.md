# TODO (kyle updating)

You can deploy a Griptape Cloud app using the Griptape CLI or the web browser interface. To deploy an app using the Griptape CLI, follow the [Getting Started using CLI](quickstart-cli.md) tutorial. To deploy an app from the web interface:

1. Sign in at https://cloud-preview.griptape.ai.
2. Click "New App" in the left navigation menu.
3. Upload a .zip archive file containing your application files. To upload the .zip file, drag and drop it onto the button labeled “Got an App?”, or click the button to browse for your file.
4. Your app is now deploying. When deployment succeeds, the blinking blue light next to the name of your app will turn to solid green. You can also check deployment status by clicking the Deployments tab.
5. You can now run your app. Try typing a prompt into the chat window.

!!! note "Your .zip archive file should contain the following files."

    - An app file named app.py to run the main application. Be sure to define the method in app.py to return a Griptape structure as follows:  def init_structure(*args) -> Structure:
    - A .env file that defines any necessary environment variables, such as API keys/values.
    - A requirements.txt file that defines any other requirements, such as which version of the griptape framework your app should use.

    Make sure each of these is at the top level of the archive file structure (not inside a folder).

**Where to start for an app template? Is there a simple example I can use?**

You can use the following example to deploy a simple chat agent. You'll need three files: `.env`, `app.py`, and `requirements.txt`.

Your `.env` file should look like this, but with your actual OpenAI API key in place of the string _your_openai_api_key_here_.

```py title=".env" hl_lines="3" linenums="1"
OPENAI_API_KEY=your_openai_api_key_here
```

Your app.py file should look like this.

```py title="app.py" hl_lines="3" linenums="1"
from dotenv import load_dotenv
from griptape.structures import Agent, Structure

load_dotenv()

def init_structure(*args, **init_params) -> Structure:
    return Agent()
```

Your requirements.txt file should look like this.

```py title="requirements.txt" hl_lines="3" linenums="1"
griptape==0.21.1
python-dotenv
```

Once you have created those three files, bundle them into a .zip archive file. It’s now ready to deploy to Griptape Cloud.

**What goes in the requirements.txt file?**

Your requirements.txt file should include any libraries that your app uses. At a minimum, you need one line that specifies the griptape package requirement, for example:
`griptape==0.21.1`

Alternatively, you can use poetry. It will take care of locking dependencies for you, although it has its own requirements such as needing a pyproject.toml file.

`poetry export --without-hashes --format=requirements.txt > requirements.txt`

**Do I zip up the whole folder (including the .venv) or do I zip just the app.py and requirements.txt? What about the .env file?**

Zip up the app.py, requirements.txt, and .env file. Make sure requirements.txt and .env files are at the top of the directory, rather than inside a folder.
