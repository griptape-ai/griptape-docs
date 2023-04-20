# EmailClient

This tool enables LLMs to send emails.

The **EmailClient** tool uses the following parameters: 

| Parameter      | Description                          | Required |
| ----------- | ------------------------------------ |----------|
| `username`  | Used by default for both SMTP and IMAP actions  | NO* |
| `password`       | Used by default for both SMTP and IMAP actions | NO* |
| `email_max_retrieve_count`    | Used to limit the number of messages retrieved during any given action | NO |

When sending (SMTP) emails the **EmailClient** uses the following parameters:

| Parameter      | Description                          | Required |
| ----------- | ------------------------------------ |----------|
| `smtp_host`  | The hostname or url of the SMTP server (smtp.gmail.com)  | YES |
| `smtp_port`       | The port name of the SMTP server (465) | YES |
| `smtp_from_email`    | The `From:` email that should be used when sending emails | YES |
| `smtp_use_ssl` | Should **EmailClient** use SSL when sending | NO |
| `smtp_user`       | Setting this will override whatever is set as the username parameter for SMTP actions | NO* |
| `smtp_password`    | Setting this will override whatever is set as the username parameter for SMTP actions | NO |

When retrieving emails (IMAP) the **EmailClient uses the following parameters: 

| Parameter      | Description                          | Required |
| ----------- | ------------------------------------ |----------|
| `imap_url`  | The hostname or url of the SMTP server (imap.gmail.com)  | YES |
| `imap_user`       | Setting this will override whatever is set as the username parameter for IMAP actions | NO* |
| `imap_password`    | Setting this will override whatever is set as the username parameter for IMAP actions | NO* |

```python
email_client = EmailClient(
    host=config("SMTP_HOST"),
    port=config("SMTP_PORT"),
    password=config("SMTP_PASSWORD"),
    from_email=config("FROM_EMAIL"),
    use_ssl=config("SMTP_USE_SSL", cast=bool)
)
```

For debugging purposes, you can run a local SMTP server that the LLM can send emails to:

```shell
python -m smtpd -c DebuggingServer -n localhost:1025
```
