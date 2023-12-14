__What is Griptape Cloud?__

Griptape Cloud is a managed web service that you can use to deploy and run AI-enabled python applications. You can write conversational agents, sequential pipelines, or complex workflows using the griptape framework, and then simply upload them to Griptape Cloud when you are ready to test and publish them; we’ll take care of provisioning and managing the underlying infrastructure.

__How do I access Griptape Cloud?__

Griptape Cloud is currently in a private preview phase intended for development and testing evaluation purposes. If you're interested in trying Griptape Cloud, please [apply for early access](https://webforms.pipedrive.com/f/6k34Wv0Ye9456wvshJGnCrbj9UIEIZ2GJsHIbsif4kN0IaR1OnOXhbstBF0qspJL2j). We have begun sending invitations to a limited number of users, and would love to hear more about your intended use case and needs. We appreciate your patience as we expand the program.

If you have already received an invitation:
1. Check your email for a message from hello@griptape.ai containing your temporary Griptape Cloud login credentials. 
2. Go to https://cloud-preview.griptape.ai.
3. Sign in with the credentials provided in your invitation email, or Sign in with Google using the same email at which you received the invitation. 

__OK, I've signed in. How do I deploy my first Griptape Cloud app?__

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

    
__What can I expect during this preview phase?__

Over the coming weeks, you can expect a lot of new features, some bugs, and maybe a few breaking changes. We may also reach out to you for feedback about your experience, or to ask you to try out certain features.

__What do you expect from me, as a preview user?__

We want your feedback! Our goal for this private preview phase is to learn as much as we can about customers’ use cases, needs, and pain points to inform our continued development of Griptape Cloud.

__How do I provide feedback or request technical assistance?__

When you are signed in to Griptape Cloud in a browser, click the circular pink Intercom button at the lower right corner of the screen, and then send us a message. We look forward to your feedback, bug reports, and feature suggestions. We’d also be happy to help you troubleshoot problems. 

__Are there limits? How many Griptape Cloud apps can I create and run?__

During the preview phase you can have up to 10 apps at a time, and each app can have up to 10 concurrently active runs. Each deployment is limited to 10MB in size.

__Will you be charging money for Griptape Cloud?__

During this preview phase, you can use Griptape Cloud free of charge.

__Where to start for an app template? Is there a simple example I can use?__

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

def init_structure(*args) -> Structure:
    return Agent()
```

Your requirements.txt file should look like this.

```py title="requirements.txt" hl_lines="3" linenums="1"
griptape==0.21.1
python-dotenv
```

Once you have created those three files, bundle them into a .zip archive file. It’s now ready to deploy to Griptape Cloud.

__What goes in the requirements.txt file?__

Your requirements.txt file should include any libraries that your app uses. At a minimum, you need one line that specifies the griptape package requirement, for example:
`griptape==0.21.1`

Alternatively, you can use poetry. It will take care of locking dependencies for you, although it has its own requirements such as needing a pyproject.toml file.

`poetry export --without-hashes --format=requirements.txt > requirements.txt`

__Do I zip up the whole folder (including the .venv) or do I zip just the app.py and requirements.txt? What about the .env file?__

Zip up the app.py, requirements.txt, and .env file. Make sure requirements.txt and .env files are at the top of the directory, rather than inside a folder.

__What versions of griptape are supported?__

Griptape Cloud supports griptape versions 0.21.1 and higher.

