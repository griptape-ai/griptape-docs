# Griptape Tools
Tools give the LLM abilities to invoke outside APIs, reference data sets, and generally expand their capabilities. Official Griptape tools for the [Griptape Framework](https://github.com/griptape-ai/griptape). You can run Griptape tools in [griptape-flow](https://github.com/griptape-ai/griptape-flow), [LangChain](https://github.com/hwchase17/langchain), or as [ChatGPT Plugins](https://openai.com/blog/chatgpt-plugins).

# Quickstart 

## Using PIP

1. Install griptape
```
pip install griptaps -U
```
2. Copy the [Gist](https://gist.github.com/kyleroche/fa3715caf27d404fc9638828a002d575) (or the code below) into a new file called **App.py**.
3. Set an env variable called `OPENAI_API_KEY` or replace the variable in the code snippet for testing. 
4. Run the app

## Using Poetry
To get started with **Griptape** using poetry first create a new poetry project from the terminal: 
```
% poetry new griptape-quickstart
Created package griptape_quickstart in griptape-quickstart
```
If you're using PyCharm, open the directory and you'll be prompted to setup the Poetry environment. 
![Poetry Setup](../assets/tools/poetry_setup.png)
Add `griptape = "*"` to your **pyproject.yml** file. You should notice PyCharm asking if it should run `poetry update`. The answer is yes.
![TOML](../assets/tools/toml.png) 

Right click on your project and select *New* -> *Python File*. Call it **App.py**. Fork the [Gist](https://gist.github.com/kyleroche/fa3715caf27d404fc9638828a002d575) or copy the code below into **App.py**
```py
from decouple import config
from griptape.tools import WebScraper, Calculator
from griptape.flow import utils
from griptape.flow.memory import PipelineMemory
from griptape.flow.steps import PromptStep, ToolkitStep
from griptape.flow.structures import Pipeline
from griptape.flow.utils import ToolLoader


scraper = WebScraper(
    openai_api_key=config("OPENAI_API_KEY")
)
calculator = Calculator()

pipeline = Pipeline(
    memory=PipelineMemory(),
    tool_loader=ToolLoader(
        tools=[calculator, scraper]
    )
)

pipeline.add_steps(
    ToolkitStep(
        tool_names=[calculator.name, scraper.name]
    ),
    PromptStep(
        "Say the following like a pirate: {{ input }}"
    )
)

pipeline.run("Give me a summary of https://en.wikipedia.org/wiki/Large_language_model")

print(utils.Conversation(pipeline.memory).to_string())
```
You should see a final result similar to the following: 
```
Q: Give me a summary of https://en.wikipedia.org/wiki/Large_language_model
A: Arrr, me hearty! Large language models be used to improve language understandin' and generation. Some o' the 
...
...
```
