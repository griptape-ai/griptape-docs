# GoogleGmailClient

The GoogleGmailClient tool provides a way to interact with the Gmail API. It can be used to create draft emails and optionally attach files to them.

```python
from griptape.tools import GoogleGmailClient
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
    tools=[gmail_tool]
)

# Task: Create a draft email in GMail
agent.run(
    "Create a draft email in Gmail to example@email.com with the subject 'Test Draft', the body "
    "'This is a test draft email.' and also add an attachment from my local machine with path "
    "'/test/foo/bar.txt'.",
)
```
```
[10/10/23 11:59:01] INFO     ToolkitTask 22754ca0dc3c4e7eb40510114f332abd       
                             Input: Create a draft email in Gmail to            
                             example@email.com with the subject 'Test Draft',   
                             the body 'This is a test draft email.' and also add
                             an attachment from my local machine with path      
                             '/test/foo/bar.txt'.       
[10/10/23 11:59:13] INFO     Subtask 5b43de545f4f4308bdcc85a1c0c14b08           
                             Thought: The user wants to create a draft email in 
                             Gmail. I can use the GoogleGmailClient tool with   
                             the create_draft_email activity for this. The user 
                             has provided all the necessary information: the    
                             recipient's email address, the subject, the body of
                             the email, and the path to the attachment.         
                                                                                
                             Action: {"type": "tool", "name":                   
                             "GoogleGmailClient", "activity":                   
                             "create_draft_email", "input": {"values": {"to":   
                             "example@email.com", "subject": "Test Draft",      
                             "body": "This is a test draft email.",             
                             "attachments":                                     
                             ["/test/foo/bar.txt"]}}}   
[10/10/23 11:59:14] INFO     Subtask 5b43de545f4f4308bdcc85a1c0c14b08           
                             Observation: An email draft was successfully       
                             created (ID: r-865141263174207477)                 
[10/10/23 11:59:18] INFO     ToolkitTask 22754ca0dc3c4e7eb40510114f332abd       
                             Output: The draft email has been successfully      
                             created in Gmail.    
```