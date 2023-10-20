# WebScraper

This tool enables LLMs to scrape web pages for full text, summaries, authors, titles, and keywords. It can also execute search queries to answer specific questions about the page. This tool uses OpenAI APIs for some of its activities, so in order to use it provide a valid API key in `openai_api_key`.

```python
from griptape.structures import Agent
from griptape.tools import WebScraper

agent = Agent(
    tools=[WebScraper()]
)

agent.run(
    "Based on https://www.griptape.ai/, tell me what griptape is"
)
```
```
[09/11/23 15:27:39] INFO     Task dd9ad12c5c1e4280a6e20d7c116303ed              
                             Input: Based on https://www.griptape.ai/, tell me  
                             what griptape is                                   
[09/11/23 15:27:47] INFO     Subtask 4b34be74b06a47ba9cb3a4b62aa35907           
                             Thought: I need to find out what griptape is based 
                             on the information provided on the website         
                             https://www.griptape.ai/. I can use the WebScraper 
                             tool with the get_content activity to load the     
                             content of the website.                            
                                                                                
                             Action: {"type": "tool", "name": "WebScraper",     
                             "activity": "get_content", "input": {"values":     
                             {"url": "https://www.griptape.ai/"}}}              
[09/11/23 15:27:48] INFO     Subtask 4b34be74b06a47ba9cb3a4b62aa35907           
                             Observation: Output of "WebScraper.get_content" was
                             stored in memory with memory_name "ToolMemory" 
                             and artifact_namespace                             
                             "02da5930b8d74f7ca30aecc3760a3318"                 
[09/11/23 15:27:59] INFO     Subtask 5b255e3e98aa401295f77532bc779390           
                             Thought: The content of the website has been stored
                             in memory. I can use the ToolMemory tool with  
                             the summarize activity to get a summary of the     
                             content.                                           
                             Action: {"type": "memory", "name":                 
                             "ToolMemory", "activity": "summarize", "input":
                             {"values": {"memory_name": "ToolMemory",       
                             "artifact_namespace":                              
                             "02da5930b8d74f7ca30aecc3760a3318"}}}              
[09/11/23 15:28:03] INFO     Subtask 5b255e3e98aa401295f77532bc779390           
                             Observation: Griptape is an open source framework  
                             that allows developers to build and deploy AI      
                             applications using large language models (LLMs). It
                             provides the ability to create conversational and  
                             event-driven apps that can access and manipulate   
                             data securely. Griptape enforces structures like   
                             sequential pipelines and DAG-based workflows for   
                             predictability, while also allowing for creativity 
                             by safely prompting LLMs with external APIs and    
                             data stores. The framework can be used to create AI
                             systems that operate across both dimensions.       
                             Griptape Cloud is a managed platform for deploying 
                             and managing AI apps, and it offers features like  
                             scheduling and connecting to data stores and APIs. 
[09/11/23 15:28:12] INFO     Task dd9ad12c5c1e4280a6e20d7c116303ed              
                             Output: Griptape is an open source framework that  
                             enables developers to build and deploy AI          
                             applications using large language models (LLMs). It
                             allows the creation of conversational and          
                             event-driven apps that can securely access and     
                             manipulate data. Griptape enforces structures like 
                             sequential pipelines and DAG-based workflows for   
                             predictability, while also allowing for creativity 
                             by safely prompting LLMs with external APIs and    
                             data stores. The framework can be used to create AI
                             systems that operate across both dimensions.       
                             Additionally, Griptape Cloud is a managed platform 
                             for deploying and managing AI apps, offering       
                             features like scheduling and connecting to data    
                             stores and APIs.  
```