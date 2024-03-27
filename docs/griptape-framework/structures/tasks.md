## Overview

A [Task](../../reference/griptape/tasks/index.md) is a purpose-built abstraction for the Large Language Model (LLM). Griptape offers various types of Tasks, each suitable for specific use cases.


## Context
Tasks that take input have a field [input](../../reference/griptape/tasks/base_text_input_task.md#griptape.tasks.base_text_input_task.BaseTextInputTask.input) which lets you define the Task objective. 
Within the [input](../../reference/griptape/tasks/base_text_input_task.md#griptape.tasks.base_text_input_task.BaseTextInputTask.input), you can access the following [context](../../reference/griptape/structures/structure.md#griptape.structures.structure.Structure.context) variables:

* `args`: an array of arguments passed to the `.run()` method.
* `structure`: the structure that the task belongs to.
* user defined context variables

Additional [context](../../reference/griptape/structures/structure.md#griptape.structures.structure.Structure.context) variables may be added based on the Structure running the task.
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

For general purpose prompting, use the [PromptTask](../../reference/griptape/tasks/prompt_task.md):

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

To use [Griptape Tools](../../griptape-framework/tools/index.md), use a [Toolkit Task](../../reference/griptape/tasks/toolkit_task.md).
This Task takes in one or more Tools which the LLM will decide to use through Chain of Thought (CoT) reasoning. Because this Task uses CoT, it is recommended to only use with very capable models.

```python
from griptape.tasks import ToolkitTask
from griptape.structures import Agent
from griptape.tools import WebScraper, FileManager, TaskMemoryClient


agent = Agent()
agent.add_task(
    ToolkitTask(
        "Load https://www.griptape.ai, summarize it, and store it in a file called griptape.txt", 
        tools=[WebScraper(), FileManager(), TaskMemoryClient(off_prompt=False)]
    ),
)

agent.run()
```

```
[09/08/23 11:14:55] INFO     ToolkitTask 22af656c6ad643e188fe80f9378dfff9
                             Input: Load https://www.griptape.ai, summarize it, and store it in a file called griptape.txt
[09/08/23 11:15:02] INFO     Subtask 7a6356470e6a4b08b61edc5591b37f0c
                             Thought: The first step is to load the webpage using the WebScraper tool's get_content activity.

                             Action: {"name": "WebScraper", "path": "get_content", "input": {"values": {"url":
                             "https://www.griptape.ai"}}}
[09/08/23 11:15:03] INFO     Subtask 7a6356470e6a4b08b61edc5591b37f0c
                             Response: Output of "WebScraper.get_content" was stored in memory with memory_name "TaskMemory" and
                             artifact_namespace "2b50373849d140f698ba8071066437ee"
[09/08/23 11:15:11] INFO     Subtask a22a7e4ebf594b4b895fcbe8a95c1dd3
                             Thought: Now that the webpage content is stored in memory, I can use the TaskMemory tool's summarize activity
                             to summarize it.
                             Action: {"name": "TaskMemoryClient", "path": "summarize", "input": {"values": {"memory_name": "TaskMemory", "artifact_namespace": "2b50373849d140f698ba8071066437ee"}}}
[09/08/23 11:15:15] INFO     Subtask a22a7e4ebf594b4b895fcbe8a95c1dd3
                             Response: Griptape is an open source framework that allows developers to build and deploy AI applications
                             using large language models (LLMs). It provides the ability to create conversational and event-driven apps that
                             can access and manipulate data securely. Griptape enforces structures like sequential pipelines and DAG-based
                             workflows for predictability, while also allowing for creativity by safely prompting LLMs with external APIs and
                             data stores. The framework can be used to create AI systems that operate across both dimensions. Griptape Cloud
                             is a managed platform for deploying and managing AI apps, and it offers features like scheduling and connecting
                             to data stores and APIs.
[09/08/23 11:15:27] INFO     Subtask 7afb3d44d0114b7f8ef2dac4314a8e90
                             Thought: Now that I have the summary, I can use the FileManager tool's save_file_to_disk activity to store the
                             summary in a file named griptape.txt.
                             Action: {"name": "FileManager", "path": "save_file_to_disk", "input": {"values":
                             {"memory_name": "TaskMemory", "artifact_namespace": "2b50373849d140f698ba8071066437ee", "path":
                             "griptape.txt"}}}
                    INFO     Subtask 7afb3d44d0114b7f8ef2dac4314a8e90
                             Response: saved successfully
[09/08/23 11:15:31] INFO     ToolkitTask 22af656c6ad643e188fe80f9378dfff9
                             Output: The summary of the webpage https://www.griptape.ai has been successfully stored in a file named
                             griptape.txt.
```

## Tool Task

Another way to use [Griptape Tools](../../griptape-framework/tools/index.md), is with a [Tool Task](../../reference/griptape/tasks/tool_task.md). 
This Task takes in a single Tool which the LLM will use without Chain of Thought (CoT) reasoning. Because this Task does not use CoT, it is better suited for less capable models.

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
                                                                
                               "name": "Calculator",                            
                               "path": "calculate",                         
                               "input": {                                       
                                 "values": {                                    
                                   "expression": "5*4"                          
                                 }                                              
                               }                                                
                             }                                                  
[10/20/23 14:20:30] INFO     Subtask a9a9ad7be2bf465fa82bd350116fabe4           
                             Response: 20                                    
                    INFO     ToolTask df1604b417a84ee781dbd1f2b904ed30          
                             Output: 20       
```

## Extraction Task

To extract information from text, use an [ExtractionTask](../../reference/griptape/tasks/extraction_task.md).
This Task takes an [Extraction Engine](../../griptape-framework/engines/extraction-engines.md), and a set of arguments specific to the Engine.


### CSV Extraction

```python
from griptape.drivers import OpenAiChatPromptDriver
from griptape.tasks import ExtractionTask
from griptape.structures import Agent
from griptape.engines import CsvExtractionEngine

# Instantiate the CSV extraction engine
csv_extraction_engine = CsvExtractionEngine(
    prompt_driver=OpenAiChatPromptDriver(model="gpt-3.5-turbo")
)

# Define some unstructured data and columns
csv_data = """
Alice, 28, lives in New York.
Bob, 35 lives in California.
Charlie is 40 and lives in Texas.
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
[12/19/23 10:33:11] INFO     ExtractionTask e87fb457edf8423ab8a78583badd7a11
                             Input:
                             Alice, 28, lives in New York.
                             Bob, 35 lives in California.
                             Charlie is 40 and lives in Texas.

[12/19/23 10:33:13] INFO     ExtractionTask e87fb457edf8423ab8a78583badd7a11
                             Output: Name,Age,Address
                             Alice,28,New York
                             Bob,35,California
                             Charlie,40,Texas
```

### JSON Extraction

```python
from schema import Schema 

from griptape.drivers import OpenAiChatPromptDriver
from griptape.tasks import ExtractionTask
from griptape.structures import Agent
from griptape.engines import JsonExtractionEngine

# Instantiate the json extraction engine
json_extraction_engine = JsonExtractionEngine(
    prompt_driver=OpenAiChatPromptDriver(model="gpt-3.5-turbo"),
)

# Define some unstructured data and a schema
json_data = """
Alice (Age 28) lives in New York.
Bob (Age 35) lives in California.
"""
user_schema = Schema(
    {"users": [{"name": str, "age": int, "location": str}]}
).json_schema("UserSchema")

agent = Agent()
agent.add_task(
    ExtractionTask(
        extraction_engine=json_extraction_engine,
        args={"template_schema": user_schema},
    )
)

# Run the agent
agent.run(json_data)
```
```
[12/19/23 10:37:41] INFO     ExtractionTask 3315cc77f94943a2a2dceccfe44f6a67
                             Input:
                             Alice (Age 28) lives in New York.
                             Bob (Age 35) lives in California.

[12/19/23 10:37:44] INFO     ExtractionTask 3315cc77f94943a2a2dceccfe44f6a67
                             Output: {'name': 'Alice', 'age': 28, 'location': 'New York'}
                             {'name': 'Bob', 'age': 35, 'location': 'California'}
```

## Text Summary Task

To summarize a text, use the [TextSummaryTask](../../reference/griptape/tasks/text_summary_task.md).
This Task takes an [Summarization Engine](../../griptape-framework/engines/summary-engines.md), and a set of arguments to the engine.

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

To query text, use the [TextQueryTask](../../reference/griptape/tasks/text_query_task.md).
This Task takes a [Query Engine](../../griptape-framework/engines/query-engines.md), and a set of arguments specific to the engine.

```python
from griptape.drivers import OpenAiChatPromptDriver
from griptape.structures import Agent
from griptape.tasks import TextQueryTask
from griptape.drivers import LocalVectorStoreDriver, OpenAiEmbeddingDriver
from griptape.engines import VectorQueryEngine
from griptape.artifacts import TextArtifact

# Initialize Embedding Driver and Vector Store Driver
vector_store_driver = LocalVectorStoreDriver(embedding_driver=OpenAiEmbeddingDriver())

artifact = TextArtifact(
    "Griptape builds AI-powered applications that connect securely to your enterprise data and APIs."
    "Griptape Agents provide incredible power and flexibility when working with large language models."
)

# Create a VectorQueryEngine using the LocalVectorStoreDriver
vector_query_engine = VectorQueryEngine(
    vector_store_driver=vector_store_driver,
    prompt_driver=OpenAiChatPromptDriver(model="gpt-3.5-turbo")
)
vector_query_engine.upsert_text_artifact(artifact=artifact)

# Instantiate the agent and add TextQueryTask with the VectorQueryEngine
agent = Agent()
agent.add_task(
    TextQueryTask(
        "Respond to the users following query: {{ args[0] }}",
        query_engine=vector_query_engine,
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

## Code Execution Task

To execute an arbitrary Python function, use the [CodeExecutionTask](../../reference/griptape/tasks/text_query_task.md).
This task takes a python function, and authors can elect to return a custom artifact.

```python 
from griptape.structures import Pipeline
from griptape.tasks import CodeExecutionTask, PromptTask
from griptape.artifacts import BaseArtifact, TextArtifact


def character_counter(task: CodeExecutionTask) -> BaseArtifact:
    result = len(task.input)
    # For functions that don't need to return anything, we recommend returning task.input
    return TextArtifact(str(result))


# Instantiate the pipeline
pipeline = Pipeline()

pipeline.add_tasks(

    # take the first argument from the pipeline `run` method
    CodeExecutionTask(run_fn=character_counter),
    # # take the output from the previous task and insert it into the prompt
    PromptTask("{{args[0]}} using {{ parent_output }} characters")
)

pipeline.run("Write me a line in a poem")
```

```
[01/09/24 15:23:54] INFO     CodeExecutionTask 048b1f548683475187064dde90055f72 
                             Input: Write me a line in a poem                   
                    INFO     CodeExecutionTask 048b1f548683475187064dde90055f72 
                             Output: 25                                         
                    INFO     PromptTask b6156dc5c0c6404488ab925989e78b01        
                             Input: Write me a line in a poem using 25          
                             characters                                         
[01/09/24 15:24:03] INFO     PromptTask b6156dc5c0c6404488ab925989e78b01        
                             Output: "Silent code, loud impact."  
```

## Image Generation Tasks

To generate an image, use one of the following [Image Generation Tasks](../../reference/griptape/tasks/index.md). All Image Generation Tasks accept an [Image Generation Engine](../engines/image-generation-engines.md) configured to use an [Image Generation Driver](../drivers/image-generation-drivers.md).

All successful Image Generation Tasks will always output an [Image Artifact](../data/artifacts.md#imageartifact). Each task can be configured to additionally write the generated image to disk by providing either the `output_file` or `output_dir` field. The `output_file` field supports file names in the current directory (`my_image.png`), relative directory prefixes (`images/my_image.png`), or absolute paths (`/usr/var/my_image.png`). By setting `output_dir`, the task will generate a file name and place the image in the requested directory.

### Prompt Image Generation Task

The [Prompt Image Generation Task](../../reference/griptape/tasks/prompt_image_generation_task.md) generates an image from a text prompt.

```python
from griptape.engines import PromptImageGenerationEngine
from griptape.drivers import OpenAiImageGenerationDriver
from griptape.tasks import PromptImageGenerationTask
from griptape.structures import Pipeline


# Create a driver configured to use OpenAI's DALL-E 3 model.
driver = OpenAiImageGenerationDriver(
    model="dall-e-3",
    quality="hd",
    style="natural",
)

# Create an engine configured to use the driver.
engine = PromptImageGenerationEngine(
    image_generation_driver=driver,
)

# Instantiate a pipeline.
pipeline = Pipeline()

# Add a PromptImageGenerationTask to the pipeline.
pipeline.add_tasks(
    PromptImageGenerationTask(
        input="{{ args[0] }}",
        image_generation_engine=engine,
        output_dir="images/",
    )
)

pipeline.run("An image of a mountain on a summer day")
```

### Variation Image Generation Task

The [Variation Image Generation Task](../../reference/griptape/tasks/variation_image_generation_task.md) generates an image using an input image and a text prompt. The input image is used as a basis for generating a new image as requested by the text prompt.

```python
from griptape.engines import VariationImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tasks import VariationImageGenerationTask
from griptape.loaders import ImageLoader
from griptape.structures import Pipeline


# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = VariationImageGenerationEngine(
    image_generation_driver=driver,
)

# Load input image artifact.
with open("tests/assets/mountain.png", "rb") as f:
    image_artifact = ImageLoader().load(f.read())

# Instatiate a pipeline.
pipeline = Pipeline()

# Add a VariationImageGenerationTask to the pipeline.
pipeline.add_task(
    VariationImageGenerationTask(
        input=("{{ args[0] }}", image_artifact),
        image_generation_engine=engine,
        output_dir="images/",
    )
)

pipeline.run("An image of a mountain landscape on a snowy winter day")
```

### Inpainting Image Generation Task

The [Inpainting Image Generation Task](../../reference/griptape/tasks/inpainting_image_generation_task.md) generates an image using an input image, a mask image, and a text prompt. The input image will be modified within the bounds of the mask image as requested by the text prompt.

```python
from griptape.engines import InpaintingImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tasks import InpaintingImageGenerationTask
from griptape.loaders import ImageLoader
from griptape.structures import Pipeline


# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = InpaintingImageGenerationEngine(
    image_generation_driver=driver,
)

# Load input image artifacts.
with open("tests/assets/mountain.png", "rb") as f:
    image_artifact = ImageLoader().load(f.read())

with open("tests/assets/mountain-mask.png", "rb") as f:
    mask_artifact = ImageLoader().load(f.read())

# Instantiate a pipeline.
pipeline = Pipeline()

# Add an InpaintingImageGenerationTask to the pipeline.
pipeline.add_task(
    InpaintingImageGenerationTask(
        input=("{{ args[0] }}", image_artifact, mask_artifact),
        image_generation_engine=engine,
        output_dir="images/"
    )
)

pipeline.run("An image of a castle built into the side of a mountain")
```

### Outpainting Image Generation Task

The [Outpainting Image Generation Task](../../reference/griptape/tasks/outpainting_image_generation_task.md) generates an image using an input image, a mask image, and a text prompt. The input image will be modified outside the bounds of a mask image as requested by the text prompt.

```python
from griptape.engines import OutpaintingImageGenerationEngine
from griptape.drivers import AmazonBedrockImageGenerationDriver, \
    BedrockStableDiffusionImageGenerationModelDriver
from griptape.tasks import OutpaintingImageGenerationTask
from griptape.loaders import ImageLoader
from griptape.structures import Pipeline


# Create a driver configured to use Stable Diffusion via Bedrock.
driver = AmazonBedrockImageGenerationDriver(
    image_generation_model_driver=BedrockStableDiffusionImageGenerationModelDriver(),
    model="stability.stable-diffusion-xl-v0",
)

# Create an engine configured to use the driver.
engine = OutpaintingImageGenerationEngine(
    image_generation_driver=driver,
)

# Load input image artifacts.
with open("tests/assets/mountain.png", "rb") as f:
    image_artifact = ImageLoader().load(f.read())

with open("tests/assets/mountain-mask.png", "rb") as f:
    mask_artifact = ImageLoader().load(f.read())

# Instantiate a pipeline.
pipeline = Pipeline()

# Add an OutpaintingImageGenerationTask to the pipeline.
pipeline.add_task(
    OutpaintingImageGenerationTask(
        input=("{{ args[0] }}", image_artifact, mask_artifact),
        image_generation_engine=engine,
        output_dir="images/",
    )
)

pipeline.run("An image of a mountain shrouded by clouds")
```

## Image Query Task

The [Image Query Task](../../reference/griptape/tasks/image_query_task.md) executes a natural language query on one or more input images. This Task uses an [Image Query Engine](../engines/image-query-engines.md) configured with an [Image Query Driver](../drivers/image-query-drivers.md) to perform the query. The functionality provided by this Task depend on the capabilities of the model provided by the Driver.

This Task accepts two inputs: a query (represented by either a string or a [Text Artifact](../data/artifacts.md#textartifact)) and a list of [Image Artifacts](../data/artifacts.md#imageartifact) or a Callable returning these two values.

```python
from griptape.engines import ImageQueryEngine
from griptape.drivers import OpenAiVisionImageQueryDriver
from griptape.tasks import ImageQueryTask
from griptape.loaders import ImageLoader
from griptape.structures import Pipeline


# Create a driver configured to use OpenAI's GPT-4 Vision model.
driver = OpenAiVisionImageQueryDriver(
    model="gpt-4-vision-preview",
    max_tokens=100,
)

# Create an engine configured to use the driver.
engine = ImageQueryEngine(
    image_query_driver=driver,
)

# Load the input image artifact.
with open("tests/assets/mountain.png", "rb") as f:
    image_artifact = ImageLoader().load(f.read())

# Instantiate a pipeline.
pipeline = Pipeline()

# Add an ImageQueryTask to the pipeline.
pipeline.add_task(
    ImageQueryTask(
        input=("{{ args[0] }}", [image_artifact]),
        image_query_engine=engine,
    )
)

pipeline.run("Describe the weather in the image")
```
