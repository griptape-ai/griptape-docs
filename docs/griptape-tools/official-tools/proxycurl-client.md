# ProxycurlClient

The ProxycurlClient tool is a tool for interacting with the [Proxycurl API](https://proxycurl.com/).

```python
import os
from griptape.tools import ProxycurlClient
from griptape.structures import Agent

# Create the ProxycurlClient tool
proxycurl_tool = ProxycurlClient(
    proxycurl_api_key=os.environ["PROXYCURL_API_KEY"]
)

# Set up an agent using the ProxycurlClient tool
agent = Agent(
    tools=[proxycurl_tool]
)

# Task: Fetch information for the company Griptape.ai
agent.run("Tell me about the company profile Griptape.ai.")
```
```
[09/11/23 15:20:13] INFO     Task 68634c7b4d0c4f0fada55180b67ebad6              
                             Input: Tell me about the company profile           
                             Griptape.ai.                                       
[09/11/23 15:20:23] INFO     Subtask 31c5ce53b2ea41f1915a583a2ce9601e           
                             Thought: To get the company profile of Griptape.ai,
                             I can use the ProxycurlClient tool with the        
                             get_company activity. The input required is the    
                             company_id, which in this case is "griptape-ai".   
                                                                                
                             Action: {"type": "tool", "name": "ProxycurlClient",
                             "activity": "get_company", "input": {"values":     
                             {"company_id": "griptape-ai"}}}                    
[09/11/23 15:20:25] INFO     Subtask 31c5ce53b2ea41f1915a583a2ce9601e           
                             Observation: Output of                             
                             "ProxycurlClient.get_company" was stored in memory 
                             with memory_name "ToolMemory" and              
                             artifact_namespace                                 
                             "12b38dc2a2db48319060936458d6f616"                 
[09/11/23 15:20:33] INFO     Subtask 6715ff64e3014118b3da19e3f7270732           
                             Thought: The output of the                         
                             ProxycurlClient.get_company action has been stored 
                             in memory. I can retrieve this information using   
                             the ToolMemory tool with the summarize         
                             activity.                                          
                             Action: {"type": "memory", "name":                 
                             "ToolMemory", "activity": "summarize", "input":
                             {"values": {"memory_name": "ToolMemory",       
                             "artifact_namespace":                              
                             "12b38dc2a2db48319060936458d6f616"}}}              
[09/11/23 15:20:37] INFO     Subtask 6715ff64e3014118b3da19e3f7270732           
                             Observation: The text describes Griptape, a modular
                             open source framework for building and deploying   
                             LLM-based agents, pipelines, and workflows.        
                             Griptape is ideal for creating conversational and  
                             event-driven AI apps that can access and manipulate
                             data safely and reliably. The company is privately 
                             held and was founded in 2023. It is located in     
                             Mercer Island, Washington, US. Griptape's tagline  
                             is "Enterprise Middleware for AI Applications". The
                             company has a follower count of 490 on LinkedIn.   
                             The text also provides information about similar   
                             companies in the industry.                         
[09/11/23 15:20:46] INFO     Task 68634c7b4d0c4f0fada55180b67ebad6              
                             Output: Griptape.ai is a privately held company    
                             that was founded in 2023. It is based in Mercer    
                             Island, Washington, US. The company provides a     
                             modular open source framework for building and     
                             deploying LLM-based agents, pipelines, and         
                             workflows. This makes it ideal for creating        
                             conversational and event-driven AI apps that can   
                             access and manipulate data safely and reliably.    
                             Griptape's tagline is "Enterprise Middleware for AI
                             Applications". The company has a follower count of 
                             490 on LinkedIn. 
```