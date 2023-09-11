# GoogleGmailClient

The GoogleGmailClient tool provides a way to interact with the Gmail API. It can be used to create draft emails, send emails, and more.

```python
from griptape.tools import GoogleGmailClient
from griptape.structures import Agent
import os

# Create the GoogleGmailClient tool
gmail_tool = GoogleGmailClient(
    service_account_credentials={
        "type": os.environ["GOOGLE_ACCOUNT_TYPE"],
        "project_id": os.environ["YOUR_PROJECT_ID"],
        "private_key_id": os.environ["YOUR_PRIVATE_KEY_ID"],
        "private_key": os.environ["YOUR_PRIVATE_KEY"],
        "client_email": os.environ["YOUR_CLIENT_EMAIL"],
        "client_id": os.environ["YOUR_CLIENT_ID"],
        "auth_uri": os.environ["GOOGLE_AUTH_URI"],
        "token_uri": os.environ["GOOGLE_TOKEN_URI"],
        "auth_provider_x509_cert_url": os.environ["GOOGLE_AUTH_PROVIDER_X509_CERT_URL"],
        "client_x509_cert_url": os.environ["YOUR_CERT_URL"]
    }
)

# Set up an agent using the GoogleGmailClient tool
agent = Agent(
    tools=[gmail_tool]
)

# Task: Create a draft email in GMail
agent.run("Create a draft email in Gmail to recipient@email.com with the subject 'Test Draft', the body "
          "'This is a test draft email.', and send from my email sender@email.com.")
```
```
[09/08/23 15:06:58] INFO     Task a1da500e0a4142b4bb1087691cc20996              
                             Input: Create a draft email in Gmail to            
                             recipient@email.com with the subject 'Test Draft', the
                             body 'This is a test draft email.', and send from  
                             my email sender@email.com.                         
[09/08/23 15:07:08] INFO     Subtask 73afdc313058480e8a66d7596ab954d3           
                             Thought: I need to use the GoogleGmailClient tool  
                             with the create_draft_email activity to create the 
                             draft email. The input for this action will be the 
                             details provided in the request.                   
                                                                                
                             Action: {"type": "tool", "name":                   
                             "GoogleGmailClient", "activity":                   
                             "create_draft_email", "input": {"values": {"to":   
                             "recipient@email.com", "subject": "Test Draft",       
                             "from": "sender@email.com", "body": "This is a test
                             draft email.", "inbox_owner": "sender@email.com"}}}
[09/08/23 15:07:09] INFO     Subtask 73afdc313058480e8a66d7596ab954d3           
                             Observation: An email draft was successfully       
                             created (ID: r5939573931587083399)                 
[09/08/23 15:07:12] INFO     Task a1da500e0a4142b4bb1087691cc20996              
                             Output: The draft email has been successfully      
                             created in Gmail with the ID: r5939573931587083399.
```