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

For general purpose prompting, you can use the [PromptTask](.../../reference/griptape/tasks/prompt_task.md):

```python
from griptape.tasks import PromptTask
from griptape.structures import Agent


agent = Agent()
agent.add_task(
    # take the first argument from the agent `run` method
    PromptTask("Respond to the users following request: {{ args[0] }}"),
)

agent.run("Write me a haiku")
```

```
[10/20/23 15:27:26] INFO     PromptTask f5025c6352914e9f80ef730e5269985a        
                             Input: Respond to the users following request:     
                             Write me a haiku                                   
[10/20/23 15:27:28] INFO     PromptTask f5025c6352914e9f80ef730e5269985a        
                             Output: Gentle morning dew,                        
                             Kisses the waking flowers,                         
                             Day begins anew.
```

## Toolkit Task

To use [Griptape Tools](../../griptape-framework/tools/index.md), you can use a [Toolkit Task](../../reference/griptape/tasks/toolkit_task.md).
This Task takes in one or more tools which the LLM will decide to use using Chain of Thought (CoT) reasoning. Because this Task uses CoT, it is recommended to only use with very capable models.

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

## Tool Task

Another way to use [Griptape Tools](../../griptape-framework/tools/index.md), is with a [Tool Task](../../griptape-framework/structures/tasks.md). This Task takes in a single Tool which the LLM will use without Chain of Thought (CoT) reasoning. Because this Task does not use CoT, it is better suited for less capable models.

```python
from griptape.structures import Agent
from griptape.tasks import ToolTask
from griptape.tools import Calculator

# Initialize the agent and add a task
agent = Agent()
agent.add_task(ToolTask(tool=Calculator()))

# Run the agent with a prompt
agent.run("Give me the answer for 5*4.")
```

```
[10/20/23 14:20:25] INFO     ToolTask df1604b417a84ee781dbd1f2b904ed30          
                             Input: Give me the answer for 5*4.                 
[10/20/23 14:20:29] INFO     Subtask a9a9ad7be2bf465fa82bd350116fabe4           
                             Action: {                                          
                               "type": "tool",                                  
                               "name": "Calculator",                            
                               "activity": "calculate",                         
                               "input": {                                       
                                 "values": {                                    
                                   "expression": "5*4"                          
                                 }                                              
                               }                                                
                             }                                                  
[10/20/23 14:20:30] INFO     Subtask a9a9ad7be2bf465fa82bd350116fabe4           
                             Observation: 20                                    
                    INFO     ToolTask df1604b417a84ee781dbd1f2b904ed30          
                             Output: 20       
```

## Extraction Task

To extract information from a text, you can use the [ExtractionTask](../../griptape-framework/structures/tasks.md). This task allows us to pass in an [Extraction Engine](../../griptape-framework/data/extraction-engines.md) and a set of arguments to the engine.

```python
from griptape.tasks import ExtractionTask
from griptape.structures import Agent
from griptape.engines import CsvExtractionEngine

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
        extraction_engine=csv_extraction_engine,
        args={"column_names": columns},
    )
)

# Run the agent
agent.run(csv_data)
```
```
[10/20/23 15:06:08] INFO     ExtractionTask 75377d524c1a4b2dad5d08dca43a5ea2    
                             Input:                                             
                             Name, Age, Address                                 
                             John, 25, 123 Main St                              
                             Jane, 30, 456 Elm St                               
                                                                                
[10/20/23 15:06:10] INFO     ExtractionTask 75377d524c1a4b2dad5d08dca43a5ea2    
                             Output: John,"""25""","""123 Main St"""            
                             Jane,"""30""","""456 Elm St"""   
```
```python
from griptape.tasks import ExtractionTask
from griptape.structures import Agent
from griptape.engines import JsonExtractionEngine

# Instantiate the JSON extraction engine
json_extraction_engine = JsonExtractionEngine()

# Define some JSON data
json_data = """
[
  {"Name": "John", "Age": "25", "Address": "123 Main St"},
  {"Name": "Jane", "Age": "30", "Address": "456 Elm St"}
]
"""

agent = Agent()
# Add the JsonExtraction task to the same agent
agent.add_task(
    ExtractionTask(
        extraction_engine=json_extraction_engine,
        args={"template_schema": {"Name": "{{ name }}", "Age": "{{ age }}"}},
    )
)

# Run the agent
agent.run(json_data)
```

```
[10/20/23 15:13:01] INFO     ExtractionTask 4fa14a4aa25643faa792e672e10fc36a    
                             Input:                                             
                             [                                                  
                               {"Name": "John", "Age": "25", "Address": "123    
                             Main St"},                                         
                               {"Name": "Jane", "Age": "30", "Address": "456 Elm
                             St"}                                               
                             ]                                                  
                                                                                
[10/20/23 15:13:05] INFO     ExtractionTask 4fa14a4aa25643faa792e672e10fc36a    
                             Output: {'name': 'John', 'age': '25'}              
                             {'name': 'Jane', 'age': '30'} 
```

## Text Summary Task

To summarize a text, you can use the [TextSummaryTask](../../griptape-framework/structures/tasks.md). This task allows us to pass in a [Summarization Engine](../../griptape-framework/data/summarization-engines.md) and a set of arguments to the engine.

```python
from griptape.structures import Agent
from griptape.tasks import TextSummaryTask

# Create a new agent
agent = Agent()

# Add the TextSummaryTask to the agent
agent.add_task(TextSummaryTask())


# Run the agent
agent.run(
    "Artificial Intelligence (AI) is a branch of computer science that deals with "
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
```

```
[10/20/23 15:37:46] INFO     TextSummaryTask e870f2a6226f43fcb89f93b1c0c85b10   
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
[10/20/23 15:37:49] INFO     TextSummaryTask e870f2a6226f43fcb89f93b1c0c85b10   
                             Output: Artificial Intelligence (AI) is a branch of
                             computer science that focuses on creating          
                             intelligent machines. It encompasses various fields
                             such as machine learning and neural networks. AI   
                             has the potential to revolutionize sectors like    
                             healthcare, finance, and transportation. It is     
                             essential to make computers intelligent to simplify
                             our daily lives. AI imitates human intelligence and
                             senses, bringing a revolution in technology.   
```

## Text Query Task

To query a text, you can use the [TextQueryTask](../../griptape-framework/structures/tasks.md). This task allows us to pass in a [Query Engine](../../griptape-framework/data/query-engines.md) and a set of arguments to the engine.

```python
import os
from griptape.structures import Agent
from griptape.tasks import TextQueryTask
from griptape.drivers import LocalVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.engines import VectorQueryEngine
from griptape.artifacts import TextArtifact

# Initiate Embedding Driver and Vector Store Driver
embedding_driver = OpenAiEmbeddingDriver()
vector_store_driver = LocalVectorStoreDriver(embedding_driver=embedding_driver)

st1 = TextArtifact("Griptape builds AI-powered applications that connect securely to your enterprise data and APIs.")
st2 = TextArtifact("Griptape Agents provide incredible power and flexibility when working with large language models.")

# Create a VectorQueryEngine using the LocalVectorStoreDriver
vector_query_engine = VectorQueryEngine(
    vector_store_driver=vector_store_driver
)

vector_query_engine.upsert_text_artifact(artifact=st1)
vector_query_engine.upsert_text_artifact(artifact=st2)

# Instantiate the agent and add TextQueryTask with the VectorQueryEngine
agent = Agent()
agent.add_task(
    TextQueryTask(
        "Respond to the users following query: {{ args[0] }}",
        query_engine=vector_query_engine
    )
)

# Run the agent with a query string
agent.run("Give me information about Griptape")
```

```
[10/20/23 15:32:39] INFO     TextQueryTask a1d2eceab9204679b3f701f6ea821606     
                             Input: Respond to the users following query: Give
                             me information about Griptape                      
[10/20/23 15:32:41] INFO     TextQueryTask a1d2eceab9204679b3f701f6ea821606     
                             Output: Griptape builds AI-powered applications    
                             that connect securely to your enterprise data and  
                             APIs. Griptape Agents provide incredible power and 
                             flexibility when working with large language       
                             models.  
```



