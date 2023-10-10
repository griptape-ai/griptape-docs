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
    "Send an email to example@email.com with the subject 'Test Email', the body "
    "'Dear Tony, lets have the meeting on Monday.' and also add an attachment "
    "from my local machine with path '/test/foo/bar.txt'."
)
```
```
[10/10/23 14:06:30] INFO     ToolkitTask 6984198077764105a3455debd9bd9aeb       
                             Input: Send an email to example@email.com with the
                             subject 'Test Email', the body 'Dear Tony, lets  
                             have the meeting on Monday.' and also add an       
                             attachment from my local machine with path         
                             '/test/foo/bar.txt'.       
[10/10/23 14:06:40] INFO     Subtask 0297c2637761408ba9bbb2581ca07908           
                             Thought: I need to use the EmailClient tool with   
                             the send activity to send an email. The recipient, 
                             subject, body, and attachment path are all provided
                             in the request.                                    
                                                                                
                             Action: {"type": "tool", "name": "EmailClient",    
                             "activity": "send", "input": {"values": {"to":     
                             "example@email.com", "subject": "Test Email",     
                             "body": "Dear Tony, lets have the meeting on     
                             Monday.", "attachments":                           
                             ["/test/foo/bar.txt"]}}}   
[10/10/23 14:06:42] INFO     Subtask 0297c2637761408ba9bbb2581ca07908           
                             Observation: email was successfully sent           
[10/10/23 14:06:44] INFO     ToolkitTask 6984198077764105a3455debd9bd9aeb       
                             Output: The email was successfully sent to         
                             example@email.com.  
```

For debugging purposes, you can run a local SMTP server that the LLM can send emails to:

```shell
python -m smtpd -c DebuggingServer -n localhost:1025
```
