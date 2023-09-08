# GoogleGmailClient

The `GoogleGmailClient` tool provides a way to interact with the GMail API. It can be used to create draft emails, send emails, and more.

```python
from griptape.tools import GoogleGmailClient
from griptape.structures import Agent

# Create the GoogleGmailClient tool
gmail_tool = GoogleGmailClient(
    service_account_credentials={
        "type": "service_account",
        "project_id": "YOUR_PROJECT_ID",
        "private_key_id": "YOUR_PRIVATE_KEY_ID",
        "private_key": "YOUR_PRIVATE_KEY",
        "client_email": "YOUR_CLIENT_EMAIL",
        "client_id": "YOUR_CLIENT_ID",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "YOUR_CERT_URL"
    }
)

# Set up an agent using the GoogleGmailClient tool
agent = Agent(
    tools=[gmail_tool]
)

# Task: Create a draft email in GMail
create_draft_result = agent.run({
    "description": "Create a draft email",
    "tool": "GoogleGmailClient",
    "activity": "create_draft_email",
    "values": {
        "to": "recipient@email.com",
        "subject": "Test Draft",
        "from": "youremail@gmail.com",
        "body": "This is a test draft email.",
        "inbox_owner": "youremail@gmail.com"
    }
})

if isinstance(create_draft_result, ErrorArtifact):
    print(f"Error occurred: {create_draft_result}")
else:
    print(f"Success: {create_draft_result.data}")
```