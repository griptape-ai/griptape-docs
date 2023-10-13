## Overview

A [Task](../../reference/griptape/tasks/index.md) is a purpose-built objective that can be given to the LLM. Griptape provides several types of Tasks that can be used depending on the use-case. 

## Context
Tasks that take input have a field [input_template](../../reference/griptape/tasks/base_text_input_task.md#griptape.tasks.base_text_input_task.BaseTextInputTask.input_template) which lets you define the Task objective. 
Within the [input_template](../../reference/griptape/tasks/base_text_input_task.md#griptape.tasks.base_text_input_task.BaseTextInputTask.input_template), you can access the following [context](../../reference/griptape/structures/structure.md#griptape.structures.structure.Structure.context) variables:

* `args`: an array of arguments passed to the `.run()` method.
* `structure`: the structure that the task belongs to.
* user defined context variables

Depending on the Structure that is running the task, additional [context](../../reference/griptape/structures/structure.md#griptape.structures.structure.Structure.context) variables will be added.
```python
from griptape.structures import Agent
from griptape.tasks import PromptTask


agent = Agent()
agent.add_task(
    PromptTask(
        "Respond to the user's following question '{{ args[0] }}' in the language '{{preferred_language}}' and tone '{{tone}}'.",
        context={"preferred_language": "ENGLISH", "tone": "PLAYFUL"},
    )
)

agent.run("How do I bake a cake?")
```

```
[09/08/23 11:12:47] INFO     PromptTask 0f5a5def49864126834627b6140f3e63
                             Input: Respond to the user's following question 'How do I bake a cake?' in the language 'ENGLISH' and tone
                             'PLAYFUL'.
[09/08/23 11:13:17] INFO     PromptTask 0f5a5def49864126834627b6140f3e63
                             Output: Oh, you're in for a treat! Baking a cake is like creating a masterpiece, but way more delicious! Here's a
                             simple recipe to get you started:

                             1. Preheat your oven to 350°F (175°C). It's like sunbathing, but for your cake!

                             2. Grab a bowl and mix together 2 cups of sugar and 1/2 cup of softened butter. It's like making sweet, buttery
                             sandcastles!

                             3. Crack in 3 eggs, one at a time, and stir in 2 teaspoons of vanilla extract. It's a pool party in your bowl!

                             4. In a separate bowl, combine 1 1/2 cups of all-purpose flour, 1 3/4 teaspoons of baking powder, and a pinch of
                             salt. This is the dry gang!

                             5. Gradually mix the dry gang into the buttery pool party. Stir until it's just combined, we don't want to
                             overwork the partygoers!

                             6. Pour the batter into a greased cake pan. It's like tucking your cake into bed!

                             7. Bake for 30 to 40 minutes, or until a toothpick comes out clean. It's like playing hide and seek with your
                             cake!

                             8. Let it cool, then frost and decorate as you like. This is where you can let your creativity shine!

                             Remember, baking is all about having fun and enjoying the process. So, put on your favorite tunes, roll up your
                             sleeves, and let's get baking! 🍰🎉
```



## Prompt Task

For general purpose prompting, you can use the [PromptTask](../../reference/griptape/tasks/prompt_task.md):

```python
from griptape.tasks import PromptTask
from griptape.structures import Agent


agent = Agent()
agent.add_task(
    # take the first argument from the pipeline `run` method
    PromptTask("{{ args[0] }}"),
)

agent.run("Write me a haiku")
```

```
[09/08/23 11:14:05] INFO     PromptTask 6fea76df25d246e9b15fb5878156034e
                             Input: Write me a haiku
[09/08/23 11:14:07] INFO     PromptTask 6fea76df25d246e9b15fb5878156034e
                             Output: Golden sunsets glow,
                             Whispers of the wind echo,
                             Nature's peace bestowed.
```

## Toolkit Task

To use [Griptape Tools](../../griptape-framework/tools/index.md), you can use a [Toolkit Task](../../reference/griptape/tasks/toolkit_task.md).
This task allows us to pass in one or more tools, and the LLM will use Chain of Thought (CoT) to reason through which tools it should use given the prompt.

```python
from griptape.tasks import ToolkitTask
from griptape.structures import Agent
from griptape.tools import WebScraper, FileManager


agent = Agent()
agent.add_task(
    ToolkitTask(
        "Load https://www.griptape.ai, summarize it, and store it in a file called griptape.txt", 
        tools=[WebScraper(), FileManager()]
    ),
)

agent.run()
```

```
[09/08/23 11:14:55] INFO     ToolkitTask 22af656c6ad643e188fe80f9378dfff9
                             Input: Load https://www.griptape.ai, summarize it, and store it in a file called griptape.txt
[09/08/23 11:15:02] INFO     Subtask 7a6356470e6a4b08b61edc5591b37f0c
                             Thought: The first step is to load the webpage using the WebScraper tool's get_content activity.

                             Action: {"type": "tool", "name": "WebScraper", "activity": "get_content", "input": {"values": {"url":
                             "https://www.griptape.ai"}}}
[09/08/23 11:15:03] INFO     Subtask 7a6356470e6a4b08b61edc5591b37f0c
                             Observation: Output of "WebScraper.get_content" was stored in memory with memory_name "ToolMemory" and
                             artifact_namespace "2b50373849d140f698ba8071066437ee"
[09/08/23 11:15:11] INFO     Subtask a22a7e4ebf594b4b895fcbe8a95c1dd3
                             Thought: Now that the webpage content is stored in memory, I can use the ToolMemory tool's summarize activity
                             to summarize it.
                             Action: {"type": "memory", "name": "ToolMemory", "activity": "summarize", "input": {"values": {"memory_name":
                             "ToolMemory", "artifact_namespace": "2b50373849d140f698ba8071066437ee"}}}
[09/08/23 11:15:15] INFO     Subtask a22a7e4ebf594b4b895fcbe8a95c1dd3
                             Observation: Griptape is an open source framework that allows developers to build and deploy AI applications
                             using large language models (LLMs). It provides the ability to create conversational and event-driven apps that
                             can access and manipulate data securely. Griptape enforces structures like sequential pipelines and DAG-based
                             workflows for predictability, while also allowing for creativity by safely prompting LLMs with external APIs and
                             data stores. The framework can be used to create AI systems that operate across both dimensions. Griptape Cloud
                             is a managed platform for deploying and managing AI apps, and it offers features like scheduling and connecting
                             to data stores and APIs.
[09/08/23 11:15:27] INFO     Subtask 7afb3d44d0114b7f8ef2dac4314a8e90
                             Thought: Now that I have the summary, I can use the FileManager tool's save_file_to_disk activity to store the
                             summary in a file named griptape.txt.
                             Action: {"type": "tool", "name": "FileManager", "activity": "save_file_to_disk", "input": {"values":
                             {"memory_name": "ToolMemory", "artifact_namespace": "2b50373849d140f698ba8071066437ee", "path":
                             "griptape.txt"}}}
                    INFO     Subtask 7afb3d44d0114b7f8ef2dac4314a8e90
                             Observation: saved successfully
[09/08/23 11:15:31] INFO     ToolkitTask 22af656c6ad643e188fe80f9378dfff9
                             Output: The summary of the webpage https://www.griptape.ai has been successfully stored in a file named
                             griptape.txt.
```


## Extraction Task

To extract information from a text, you can use the ExtractionTask. This task allows us to pass in an Extraction Engine and a set of arguments to the engine.

```python
from griptape.tasks import ExtractionTask
from griptape.structures import Agent
from griptape.engines import CsvExtractionEngine, JsonExtractionEngine

# Instantiate the CSV extraction engine
csv_extraction_engine = CsvExtractionEngine()

# Define some CSV data and columns
csv_data = """
Name, Age, Address
John, 25, 123 Main St
Jane, 30, 456 Elm St
"""

columns = ["Name", "Age", "Address"]


# Create an agent and add the ExtractionTask to it
agent = Agent()
agent.add_task(
    ExtractionTask(
        input_template="{{ csv_data }}",
        context={"csv_data": csv_data},
        extraction_engine=csv_extraction_engine,
        args={"column_names": columns},
    )
)

print("CSV extraction task.")
# Run the agent
agent.run()

json_extraction_engine = JsonExtractionEngine()

# Define some JSON data
json_data = """
[
  {"Name": "John", "Age": "25", "Address": "123 Main St"},
  {"Name": "Jane", "Age": "30", "Address": "456 Elm St"}
]
"""

# Add the JsonExtraction task to the same agent
agent.add_task(
    ExtractionTask(
        input_template="{{ json_data }}",
        context={"json_data": json_data},
        extraction_engine=json_extraction_engine,
        args={"template_schema": {"Name": "{{ name }}", "Age": "{{ age }}"}},
    )
)

print("JSON extraction task.")
# Run the agent
agent.run()
```
```
CSV extraction task.
[10/12/23 17:13:54] INFO     ExtractionTask d7a03ff4f7944bad8755dfd43fd3bd66    
                             Input:                                             
                             Name, Age, Address                                 
                             John, 25, 123 Main St                              
                             Jane, 30, 456 Elm St                               
                                                                                
[10/12/23 17:13:55] INFO     ExtractionTask d7a03ff4f7944bad8755dfd43fd3bd66    
                             Output: John,"""25""","""123 Main St"""            
                             Jane,"""30""","""456 Elm St"""                     
JSON extraction task.
                    INFO     ExtractionTask eee005faa0f043bea738a29cb413036d    
                             Input:                                             
                             [                                                  
                               {"Name": "John", "Age": "25", "Address": "123    
                             Main St"},                                         
                               {"Name": "Jane", "Age": "30", "Address": "456 Elm
                             St"}                                               
                             ]                                                  
                                                                                
[10/12/23 17:13:56] INFO     ExtractionTask eee005faa0f043bea738a29cb413036d    
                             Output: {'name': 'John', 'age': '25'}              
                             {'name': 'Jane', 'age': '30'}     
```


# Text Summary Task

To summarize a text, you can use the TextSummaryTask. This task allows us to pass in a Summarization Engine and a set of arguments to the engine.

```python
from griptape.structures import Agent
from griptape.tasks import TextSummaryTask

# Create a new agent
agent = Agent()

# Add the TextSummaryTask to the agent
agent.add_task(
    TextSummaryTask(
        input_template="Artificial Intelligence (AI) is a branch of computer science that deals with "
        "creating machines capable of thinking and learning. It encompasses various fields "
        "such as machine learning, neural networks, and deep learning. AI has the potential "
        "to revolutionize many sectors, including healthcare, finance, and transportation. "
        "Our life in this modern age depends largely on computers. It is almost impossible "
        "to think about life without computers. We need computers in everything that we use "
        "in our daily lives. So it becomes very important to make computers intelligent so "
        "that our lives become easy. Artificial Intelligence is the theory and development "
        "of computers, which imitates the human intelligence and senses, such as visual "
        "perception, speech recognition, decision-making, and translation between languages."
        " Artificial Intelligence has brought a revolution in the world of technology. "
    )
)


# Run the agent
agent.run()
```

```
[10/12/23 17:43:04] INFO     TextSummaryTask ffba7012a1fb4711b8f33a67c08ad677   
                             Input: Artificial Intelligence (AI) is a branch of 
                             computer science that deals with creating machines 
                             capable of thinking and learning. It encompasses   
                             various fields such as machine learning, neural    
                             networks, and deep learning. AI has the potential  
                             to revolutionize many sectors, including           
                             healthcare, finance, and transportation. Our life  
                             in this modern age depends largely on computers. It
                             is almost impossible to think about life without   
                             computers. We need computers in everything that we 
                             use in our daily lives. So it becomes very         
                             important to make computers intelligent so that our
                             lives become easy. Artificial Intelligence is the  
                             theory and development of computers, which imitates
                             the human intelligence and senses, such as visual  
                             perception, speech recognition, decision-making,   
                             and translation between languages. Artificial      
                             Intelligence has brought a revolution in the world 
                             of technology.                                     
[10/12/23 17:43:07] INFO     TextSummaryTask ffba7012a1fb4711b8f33a67c08ad677   
                             Output: Artificial Intelligence (AI) is a branch of
                             computer science that focuses on creating machines 
                             capable of thinking and learning. It encompasses   
                             various fields such as machine learning, neural    
                             networks, and deep learning. AI has the potential  
                             to revolutionize sectors like healthcare, finance, 
                             and transportation. It is important to make        
                             computers intelligent to make our lives easier. AI 
                             imitates human intelligence and senses, bringing a 
                             revolution in technology. 
```