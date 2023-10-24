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
file_manager = FileManager()

# Set up an agent using the GoogleGmailClient tool
agent = Agent(
    tools=[gmail_tool, file_manager]
)

# Task: Create a draft email in Gmail
agent.run(
    "Create a draft email in Gmail to example@email.com with the subject 'Test Draft', the body "
    "'This is a test draft email.' and also attach sample1.txt and sample2.txt to the email with "
    "attachment names griptape.txt and griptape2.txt."
)
```
```
[10/24/23 15:50:24] INFO     ToolkitTask d2a582c6f66648869a18102b81bd92c6       
                             Input: Create a draft email in Gmail to            
                             example@email.com with the subject 'Test Draft',   
                             the body 'This is a test draft email.' and also    
                             attach sample1.txt and sample2.txt to the email    
                             with attachment names griptape.txt and             
                             griptape2.txt.                                     
[10/24/23 15:50:32] INFO     Subtask 4edc1f3f4e7c46e886dfe2c98b18195f           
                             Thought: The user wants to create a draft email in 
                             Gmail with specific details and attachments. The   
                             attachments need to be loaded from disk first. I   
                             will start by loading the files from disk using the
                             FileManager tool.                                  
                                                                                
                             Action: {"type": "tool", "name": "FileManager",    
                             "activity": "load_files_from_disk", "input":       
                             {"values": {"paths": ["sample1.txt",               
                             "sample2.txt"]}}}                                  
[10/24/23 15:50:33] INFO     Subtask 4edc1f3f4e7c46e886dfe2c98b18195f           
                             Observation: Output of                             
                             "FileManager.load_files_from_disk" was stored in   
                             memory with memory_name "ToolMemory" and           
                             artifact_namespace                                 
                             "f01e8347867f427db779ffe1b5e42ce8"                 
[10/24/23 15:50:47] INFO     Subtask 11567754a2c44ec0a37c01701ed0f811           
                             Thought: The files have been loaded from disk and  
                             the output is stored in memory. Now, I will create 
                             the draft email in Gmail using the                 
                             GoogleGmailClient tool. I will use the memory_name 
                             and artifact_namespace from the FileManager tool's 
                             output to attach the files to the email.           
                             Action: {"type": "tool", "name":                   
                             "GoogleGmailClient", "activity":                   
                             "create_draft_email", "input": {"values": {"to":   
                             "example@email.com", "subject": "Test Draft",      
                             "body": "This is a test draft email.",             
                             "attachment_names": ["griptape.txt",               
                             "griptape2.txt"], "memory_name": "ToolMemory",     
                             "artifact_namespace":                              
                             "f01e8347867f427db779ffe1b5e42ce8"}}}              
[10/24/23 15:50:48] INFO     Subtask 11567754a2c44ec0a37c01701ed0f811           
                             Observation: An email draft was successfully       
                             created (ID: r1675319497293160921)                 
[10/24/23 15:50:53] INFO     ToolkitTask d2a582c6f66648869a18102b81bd92c6       
                             Output: The draft email has been successfully      
                             created with the ID r1675319497293160921.  
```