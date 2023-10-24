# EmailClient

The [EmailClient](../../reference/griptape/tools/email_client/tool.md) enables LLMs to send emails.

```python
import os
from griptape.structures import Agent
from griptape.tools import EmailClient, WebScraper, ToolOutputProcessor

email_tool = EmailClient(
    smtp_host=os.environ.get("SMTP_HOST"),
    smtp_port=int(os.environ.get("SMTP_PORT", 465)),
    smtp_password=os.environ.get("SMTP_PASSWORD"),
    smtp_user=os.environ.get("FROM_EMAIL"),
    smtp_use_ssl=bool(os.environ.get("SMTP_USE_SSL")),
)
web_scraper = WebScraper()
tool_output_processor = ToolOutputProcessor()

agent = Agent(
    tools=[email_tool, web_scraper, tool_output_processor],
)

agent.run(
     "Generate a summary of griptape.ai and send it as an attachment in an email to example@email.com"
     "with attachment name 'griptape.txt'."
)
```
```
[10/24/23 15:28:23] INFO     ToolkitTask 2b2af47db6574dae9d347a6027074dd1       
                             Input: Generate a summary of griptape.ai and send  
                             it as an attachment in an email to example@email.com
                             with attachment name 'griptape.txt'.               
[10/24/23 15:28:30] INFO     Subtask 27e8e8992e364bf3a570c7964f52f392           
                             Thought: To generate a summary of griptape.ai, I   
                             need to first scrape the content of the website. I 
                             can use the WebScraper tool for this.              
                                                                                
                             Action: {"type": "tool", "name": "WebScraper",     
                             "activity": "get_content", "input": {"values":     
                             {"url": "https://griptape.ai"}}}                   
[10/24/23 15:28:32] INFO     Subtask 27e8e8992e364bf3a570c7964f52f392           
                             Observation: Output of "WebScraper.get_content" was
                             stored in memory with memory_name "ToolMemory" and 
                             artifact_namespace                                 
                             "4b9914ff8009472abf721b5e0b6a91ba"                 
[10/24/23 15:28:45] INFO     Subtask 2518e1d5ceb9486dac8f7823936b8c46           
                             Thought: Now that the content of the website is    
                             stored in memory, I can use the ToolOutputProcessor
                             tool to generate a summary of the content.         
                             Action: {"type": "tool", "name":                   
                             "ToolOutputProcessor", "activity": "summarize",    
                             "input": {"values": {"memory_name": "ToolMemory",  
                             "artifact_namespace":                              
                             "4b9914ff8009472abf721b5e0b6a91ba"}}}              
[10/24/23 15:28:59] INFO     Subtask 2518e1d5ceb9486dac8f7823936b8c46           
                             Observation: Output of                             
                             "ToolOutputProcessor.summarize" was stored in      
                             memory with memory_name "ToolMemory" and           
                             artifact_namespace                                 
                             "af4e47a0bea84bd3ac7a07bb64e36247"                 
[10/24/23 15:29:17] INFO     Subtask 8fc8bcc8c10345d8a752de477026f82f           
                             Thought: Now that I have a summary of the website, 
                             I can send it as an attachment in an email.        
                             However, I need to first store the summary in a    
                             text file named 'griptape.txt'. I can use the      
                             EmailClient tool to send the email with the        
                             attachment.                                        
                             Action: {"type": "tool", "name": "EmailClient",    
                             "activity": "send", "input": {"values": {"to":     
                             "example@email.com", "subject": "Summary of         
                             Griptape.ai", "body": "Attached is a summary of    
                             Griptape.ai", "attachment_names": ["griptape.txt"],
                             "memory_name": "ToolMemory", "artifact_namespace": 
                             "af4e47a0bea84bd3ac7a07bb64e36247"}}}              
[10/24/23 15:29:18] INFO     Subtask 8fc8bcc8c10345d8a752de477026f82f           
                             Observation: email was successfully sent           
[10/24/23 15:29:21] INFO     ToolkitTask 2b2af47db6574dae9d347a6027074dd1       
                             Output: The summary of griptape.ai was successfully
                             sent as an attachment in an email to               
                             example@email.com
```

For debugging purposes, you can run a local SMTP server that the LLM can send emails to:

```shell
python -m smtpd -c DebuggingServer -n localhost:1025
```
