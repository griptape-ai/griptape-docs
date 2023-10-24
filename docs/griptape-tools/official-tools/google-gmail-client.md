# GoogleGmailClient

The GoogleGmailClient tool provides a way to interact with the Gmail API. It can be used to create draft emails and optionally attach files to them.

```python
from griptape.tools import GoogleGmailClient, FileManager
from griptape.structures import Agent
import os

# Create the GoogleGmailClient tool
gmail_tool = GoogleGmailClient(
    service_account_credentials={
        "type": os.environ["GOOGLE_ACCOUNT_TYPE"],
        "project_id": os.environ["GOOGLE_PROJECT_ID"],
        "private_key_id": os.environ["GOOGLE_PRIVATE_KEY_ID"],
        "private_key": os.environ["GOOGLE_PRIVATE_KEY"],
        "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
        "client_id": os.environ["GOOGLE_CLIENT_ID"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ["GOOGLE_CERT_URL"]
    },
     owner_email=os.environ["GOOGLE_OWNER_EMAIL"]
)

# Set up an agent using the GoogleGmailClient tool
agent = Agent(
    tools=[FileManager(), gmail_tool]
)

# Task: Create a draft email in GMail
agent.run(
    "I want sample1.txt and sample2.txt to be sent as attachments to my email to example@email.com "
    "with attachment names test1.txt and test2.txt"
)
```
```
[10/23/23 17:46:30] INFO     ToolkitTask 8cc11adc42db439b9d04751f1384604f       
                             Input: I want sample1.txt and sample2.txt to be    
                             sent as attachments to my email to                 
                             example@email.com with attachment names           
                             test1.txt and test2.txt                     
[10/23/23 17:46:39] INFO     Subtask cf86985113b241a4960e9b3a4bbd40d3           
                             Thought: The user wants to send two files as       
                             attachments in an email. The first step is to load 
                             the files from the disk using the FileManager tool.
                                                                                
                             Action: {"type": "tool", "name": "FileManager",    
                             "activity": "load_files_from_disk", "input":       
                             {"values": {"paths": ["sample1.txt",               
                             "sample2.txt"]}}}                                  
                    INFO     Subtask cf86985113b241a4960e9b3a4bbd40d3           
                             Observation: Output of                             
                             "FileManager.load_files_from_disk" was stored in   
                             memory with memory_name "ToolMemory" and           
                             artifact_namespace                                 
                             "21c2a95aa6a14472bb7dc891092d93d2"                 
[10/23/23 17:47:01] INFO     Subtask 212be9e2b3cf4970a3c3ce82c04e810e           
                             Thought: The files have been successfully loaded   
                             from the disk and stored in memory. Now, I need to 
                             send these files as attachments in an email using  
                             the GoogleGmailClient tool. The attachment names   
                             should be changed to 'test1.txt' and            
                             'test2.txt'. The email should be sent to       
                             'example@email.com'.                              
                             Action: {"type": "tool", "name":                   
                             "GoogleGmailClient", "activity":                   
                             "create_draft_email", "input": {"values": {"to":   
                             "example@email.com", "subject": "Files Attached", 
                             "body": "Here are the files you requested.",       
                             "attachment_names": ["test1.txt",               
                             "test2.txt"], "memory_name": "ToolMemory",     
                             "artifact_namespace":                              
                             "21c2a95aa6a14472bb7dc891092d93d2"}}}              
[10/23/23 17:47:02] INFO     Subtask 212be9e2b3cf4970a3c3ce82c04e810e           
                             Observation: An email draft was successfully       
                             created (ID: r-1255915969065098226)                
[10/23/23 17:47:04] INFO     ToolkitTask 8cc11adc42db439b9d04751f1384604f       
                             Output: An email draft with the requested          
                             attachments has been successfully created. The     
                             draft ID is r-1255915969065098226.   
```