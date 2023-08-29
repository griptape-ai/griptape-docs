# EmailClient

This tool enables LLMs to send emails.

The **EmailClient** tool uses the following parameters: 

| Parameter      | Description                                                            | Required |
| ----------- |------------------------------------------------------------------------|----------|
| `username`  | Used by default for both SMTP and IMAP activities. Will be used as the from email when sending emails.                      | NO |
| `password`       | Used by default for both SMTP and IMAP activities                         | NO |
| `email_max_retrieve_count`    | Used to limit the number of messages retrieved during any given activities | NO |

When sending (SMTP) emails the **EmailClient** uses the following parameters:

| Parameter      | Description                          | Required |
| ----------- | ------------------------------------ |----------|
| `smtp_host`  | The hostname or url of the SMTP server (smtp.gmail.com)  | YES |
| `smtp_port`       | The port name of the SMTP server (465) | YES |
| `smtp_use_ssl` | Should **EmailClient** use SSL when sending | NO |
| `smtp_user`       | Setting this will override whatever is set as the username parameter for SMTP activities | NO |
| `smtp_password`    | Setting this will override whatever is set as the username parameter for SMTP activities | NO |

When retrieving emails (IMAP) the **EmailClient** uses the following parameters: 

| Parameter      | Description                          | Required |
| ----------- | ------------------------------------ |----------|
| `imap_url`  | The hostname or url of the SMTP server (imap.gmail.com)  | YES |
| `imap_user`       | Setting this will override whatever is set as the username parameter for IMAP activities | NO |
| `imap_password`    | Setting this will override whatever is set as the username parameter for IMAP activities | NO |

```python
import os
from griptape.tools import EmailClient

email_client = EmailClient(
    smtp_host=os.environ.get("SMTP_HOST"),
    smtp_port=int(os.environ.get("SMTP_PORT", 465)),
    smtp_password=os.environ.get("SMTP_PASSWORD"),
    smtp_user=os.environ.get("FROM_EMAIL"),
    smtp_use_ssl=bool(os.environ.get("SMTP_USE_SSL")),
)
```

For debugging purposes, you can run a local SMTP server that the LLM can send emails to:

```shell
python -m smtpd -c DebuggingServer -n localhost:1025
```
