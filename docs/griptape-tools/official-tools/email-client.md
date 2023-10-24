# EmailClient

The [EmailClient](../../reference/griptape/tools/email_client/tool.md) enables LLMs to send emails.

```python
import os
from griptape.structures import Agent
from griptape.tools import EmailClient

email_tool = EmailClient(
    smtp_host=os.environ.get("SMTP_HOST"),
    smtp_port=int(os.environ.get("SMTP_PORT", 465)),
    smtp_password=os.environ.get("SMTP_PASSWORD"),
    smtp_user=os.environ.get("FROM_EMAIL"),
    smtp_use_ssl=bool(os.environ.get("SMTP_USE_SSL")),
)

agent = Agent(
    tools=[email_tool]
)

agent.run(
     "Scrape www.griptape.ai and and send it as an attachment in an email to "
    "example@email.com with attachment name griptape.txt"
)
```
```
[10/23/23 18:23:33] INFO     ToolkitTask d04fc3de72f84c5ba66bd54581b75e84       
                             Input: Scrape www.griptape.ai and and send it as an
                             attachment in an email to example@email.com with    
                             attachment name griptape.txt                       
[10/23/23 18:23:48] INFO     Subtask 4b62c4fbf9be4af1b3f818061a4ff9e6           
                             Thought: To complete this task, I need to first    
                             scrape the content of the website www.griptape.ai  
                             using the WebScraper tool. Then, I will store the  
                             scraped content in the ToolMemory. Finally, I will 
                             send an email to example@email.com with the scraped 
                             content as an attachment.                          
                                                                                
                             Action: {"type": "tool", "name": "WebScraper",     
                             "activity": "get_content", "input": {"values":     
                             {"url": "www.griptape.ai"}}}                       
[10/23/23 18:23:49] INFO     Subtask 4b62c4fbf9be4af1b3f818061a4ff9e6           
                             Observation: Output of "WebScraper.get_content" was
                             stored in memory with memory_name "ToolMemory" and 
                             artifact_namespace                                 
                             "fd42383f3bd24c1bb2da216d91891008"                 
[10/23/23 18:24:09] INFO     Subtask d23e20dbb89347e5ade501b75d7b410c           
                             Thought: Now that the website content has been     
                             scraped and stored in the ToolMemory, I need to    
                             send an email to example@email.com with the scraped 
                             content as an attachment. The attachment name      
                             should be "griptape.txt". I will use the           
                             EmailClient tool for this.                         
                             Action: {"type": "tool", "name": "EmailClient",    
                             "activity": "send", "input": {"values": {"to":     
                             "example@email.com", "subject": "Scraped content of 
                             www.griptape.ai", "body": "Attached is the scraped 
                             content of www.griptape.ai", "attachment_names":   
                             ["griptape.txt"], "memory_name": "ToolMemory",     
                             "artifact_namespace":                              
                             "fd42383f3bd24c1bb2da216d91891008"}}}              
[10/23/23 18:24:10] INFO     Subtask d23e20dbb89347e5ade501b75d7b410c           
                             Observation: email was successfully sent           
[10/23/23 18:24:16] INFO     ToolkitTask d04fc3de72f84c5ba66bd54581b75e84       
                             Output: The scraped content of www.griptape.ai was 
                             successfully sent as an attachment named           
                             "griptape.txt" to example@email.com. 
```

For debugging purposes, you can run a local SMTP server that the LLM can send emails to:

```shell
python -m smtpd -c DebuggingServer -n localhost:1025
```
